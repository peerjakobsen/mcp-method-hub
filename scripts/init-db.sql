-- Database initialization script for PostgreSQL
-- This script ensures proper database and user setup

-- Create database if it doesn't exist
SELECT 'CREATE DATABASE mcp_method_hub'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mcp_method_hub')\gexec

-- Create user if it doesn't exist
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_user WHERE usename = 'mcp_user') THEN
        CREATE USER mcp_user WITH PASSWORD 'mcp_password';
    END IF;
END
$$;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE mcp_method_hub TO mcp_user;
ALTER USER mcp_user CREATEDB;
