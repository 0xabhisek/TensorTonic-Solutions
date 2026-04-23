SELECT 
username, session_count, 
CASE WHEN session_count >= 50 THEN 'Power'
    WHEN session_count >=10 THEN 'Casual'
    ELSE 'Dormant' END AS activity_level,
CASE WHEN platform IN ('ios', 'android') THEN 'Mobile'
    WHEN platform IN ('web','desktop') THEN 'Desktop'
    ELSE 'Other' END AS platform_type
FROM user_sessions
ORDER BY CASE WHEN activity_level = 'Power' THEN 1
    WHEN activity_level = 'Casual' THEN 2
    ELSE 3 END, username
