# 511 Game Play Analysis I
🔹 SQL Solution
SELECT 
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;

✅ Explanation

MIN(event_date) finds the earliest date each player logged in.

GROUP BY player_id ensures we get one row per player.