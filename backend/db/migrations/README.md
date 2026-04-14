# Database Migrations

This directory is for SQL migration files (`.sql`) or Go-based migration scripts.

## How to manage migrations

1.  **GORM AutoMigrate**: Currently used in `main.go`. Best for rapid prototyping.
2.  **Explicit Migrations**: For production, use tools like `golang-migrate` or `atlas`.
    -   Store files here as `000001_init.up.sql`, `000001_init.down.sql`, etc.

## AI Agent Instructions
- When adding new tables or fields, ensure both GORM models and migration files are synchronized.
- Always check the current DB schema before proposing changes.
