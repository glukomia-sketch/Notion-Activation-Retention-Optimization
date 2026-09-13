CREATE OR REPLACE TABLE mart_funnel AS
WITH user_steps AS (
    SELECT
        u.user_id,
        u.acquisition_channel,

        MAX(CASE WHEN e.event_name = 'signup'
            THEN 1 ELSE 0 END) AS reached_signup,

        MAX(CASE WHEN e.event_name = 'onboarding_started'
            THEN 1 ELSE 0 END) AS reached_onboarding,

        MAX(CASE WHEN e.event_name = 'workspace_created'
            THEN 1 ELSE 0 END) AS reached_workspace,

        MAX(CASE WHEN e.event_name = 'content_created'
            THEN 1 ELSE 0 END) AS reached_content,

        MAX(CASE WHEN e.event_name = 'collaboration'
            THEN 1 ELSE 0 END) AS reached_collaboration,

        MAX(CASE WHEN s.paid_start_date IS NOT NULL
            THEN 1 ELSE 0 END) AS reached_paid

    FROM stg_users u
    LEFT JOIN stg_events e
        ON u.user_id = e.user_id
    LEFT JOIN stg_subscriptions s
        ON u.user_id = s.user_id

    GROUP BY
        u.user_id,
        u.acquisition_channel
)

SELECT
    acquisition_channel,

    COUNT(*) AS total_users,

    SUM(reached_signup) AS signup_users,
    SUM(reached_onboarding) AS onboarding_users,
    SUM(reached_workspace) AS workspace_users,
    SUM(reached_content) AS content_users,
    SUM(reached_collaboration) AS collaboration_users,
    SUM(reached_paid) AS paid_users,

    ROUND(
        SUM(reached_onboarding) * 1.0 /
        NULLIF(SUM(reached_signup), 0), 4
    ) AS signup_to_onboarding_rate,

    ROUND(
        SUM(reached_workspace) * 1.0 /
        NULLIF(SUM(reached_onboarding), 0), 4
    ) AS onboarding_to_workspace_rate,

    ROUND(
        SUM(reached_content) * 1.0 /
        NULLIF(SUM(reached_workspace), 0), 4
    ) AS workspace_to_content_rate,

    ROUND(
        SUM(reached_collaboration) * 1.0 /
        NULLIF(SUM(reached_content), 0), 4
    ) AS content_to_collaboration_rate,

    ROUND(
        SUM(reached_collaboration) * 1.0 /
        NULLIF(SUM(reached_signup), 0), 4
    ) AS activation_rate,

    ROUND(
        SUM(reached_paid) * 1.0 /
        NULLIF(SUM(reached_collaboration), 0), 4
    ) AS activation_to_paid_rate,

    ROUND(
        SUM(reached_paid) * 1.0 /
        NULLIF(SUM(reached_signup), 0), 4
    ) AS overall_conversion_rate

FROM user_steps

GROUP BY ROLLUP(acquisition_channel);
