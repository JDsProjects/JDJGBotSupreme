CREATE TABLE IF NOT EXISTS global_link(
    guild_id BIGINT PRIMARY KEY,
    channel_id BIGINT,
    webhook_url TEXT DEFAULT NULL
);
