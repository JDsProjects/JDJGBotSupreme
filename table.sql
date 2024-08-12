CREATE TABLE global_link IF NOT EXISTS(
    guild_id BIGINT PRIMARY KEY,
    channel_id BIGINT,
    webhook_url TEXT DEFAULT NULL
);
