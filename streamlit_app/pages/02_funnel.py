import streamlit as st
import plotly.express as px

from utils.data_loader import load_mart



st.set_page_config(
    page_title="Activation Funnel",
    page_icon="📊",
    layout="wide",
)

st.title("Notion Activation Funnel")
st.markdown(
    "Analyze user drop-offs across onboarding and product activation."
)


# Load funnel data
df = load_mart("mart_funnel")


# Remove overall total row for channel-level analysis
channel_df = df[df["acquisition_channel"].notna()].copy()


# ---------------------------------------------------------
# Overall activation funnel
# ---------------------------------------------------------

st.subheader("User Activation Journey")

funnel_data = {
    "Stage": [
        "Signup",
        "Onboarding Started",
        "Workspace Created",
        "Content Created",
        "Collaboration",
        "Paid",
    ],
    "Users": [
        channel_df["signup_users"].sum(),
        channel_df["onboarding_users"].sum(),
        channel_df["workspace_users"].sum(),
        channel_df["content_users"].sum(),
        channel_df["collaboration_users"].sum(),
        channel_df["paid_users"].sum(),
    ],
}

funnel_df = __import__("pandas").DataFrame(funnel_data)

fig = px.funnel(
    funnel_df,
    x="Users",
    y="Stage",
    title="Signup → Collaboration → Paid",
)

st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------------------------
# Activation KPIs
# ---------------------------------------------------------

st.subheader("Activation KPIs")

col1, col2, col3 = st.columns(3)

total_signup = funnel_df.loc[
    funnel_df["Stage"] == "Signup", "Users"
].iloc[0]

total_collaboration = funnel_df.loc[
    funnel_df["Stage"] == "Collaboration", "Users"
].iloc[0]

total_paid = funnel_df.loc[
    funnel_df["Stage"] == "Paid", "Users"
].iloc[0]

activation_rate = (
    total_collaboration / total_signup
    if total_signup > 0
    else 0
)

paid_rate = (
    total_paid / total_signup
    if total_signup > 0
    else 0
)

activation_to_paid = (
    total_paid / total_collaboration
    if total_collaboration > 0
    else 0
)


col1.metric(
    "Activation Rate",
    f"{activation_rate:.1%}",
)

col2.metric(
    "Signup → Paid",
    f"{paid_rate:.1%}",
)

col3.metric(
    "Activation → Paid",
    f"{activation_to_paid:.1%}",
)


# ---------------------------------------------------------
# Stage-level drop-offs
# ---------------------------------------------------------

st.subheader("Activation Drop-offs")

dropoff_data = []

for i in range(len(funnel_df) - 1):
    current_stage = funnel_df.iloc[i]
    next_stage = funnel_df.iloc[i + 1]

    current_users = current_stage["Users"]
    next_users = next_stage["Users"]

    dropoff = (
        (current_users - next_users) / current_users
        if current_users > 0
        else 0
    )

    dropoff_data.append(
        {
            "From": current_stage["Stage"],
            "To": next_stage["Stage"],
            "Drop-off Rate": dropoff,
        }
    )

dropoff_df = __import__("pandas").DataFrame(dropoff_data)

st.dataframe(
    dropoff_df.style.format(
        {"Drop-off Rate": "{:.1%}"}
    ),
    use_container_width=True,
)


# ---------------------------------------------------------
# Channel comparison
# ---------------------------------------------------------

st.subheader("Activation by Acquisition Channel")

channel_display = channel_df[
    [
        "acquisition_channel",
        "signup_users",
        "collaboration_users",
        "activation_rate",
        "overall_conversion_rate",
    ]
].copy()

channel_display.columns = [
    "Acquisition Channel",
    "Signups",
    "Activated Users",
    "Activation Rate",
    "Paid Conversion Rate",
]

st.dataframe(
    channel_display.style.format(
        {
            "Activation Rate": "{:.1%}",
            "Paid Conversion Rate": "{:.1%}",
        }
    ),
    use_container_width=True,
)


# ---------------------------------------------------------
# PM opportunity
# ---------------------------------------------------------

st.subheader("PM Opportunity")

worst_stage = dropoff_df.loc[
    dropoff_df["Drop-off Rate"].idxmax()
]

st.info(
    f"The largest activation drop-off occurs between "
    f"**{worst_stage['From']}** and **{worst_stage['To']}** "
    f"({worst_stage['Drop-off Rate']:.1%}). "
    "This stage represents a priority opportunity for onboarding "
    "and product experience improvements."
)
