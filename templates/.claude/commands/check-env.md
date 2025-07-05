# Check Environment Variables Command

Check if all required environment variables are properly configured.

## Steps:

1. **Check for .env file**
   - If missing, look for .env.example
   - List all required variables

2. **Validate each variable**
   - Check if set and non-empty
   - Flag any missing or placeholder values

3. **Report findings**
   ```
   ✅ DATABASE_URL - Set
   ❌ API_KEY - Missing
   ⚠️  SMTP_PASSWORD - Using placeholder value
   ```

4. **Provide instructions**
   - Which variables need attention
   - Where to get API keys
   - Security reminders

## Example Usage:
When AI needs an API key or environment variable, it can run:
```
/check-env
```

This helps identify missing configuration before runtime errors occur.