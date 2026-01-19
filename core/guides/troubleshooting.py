# core/guides/troubleshooting.py
# Troubleshooting Guide (v3.0.0)

"""
Troubleshooting Guide.

Provides practical guidance on diagnosing and resolving common
development issues and system problems.

Introduced in v3.0.0.
"""

GUIDE_ID = "troubleshooting"

GUIDE = {
    "title": "Troubleshooting Guide",
    "purpose": "Learn how to diagnose and resolve common issues",
    "audience": "All developers",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["contributing", "code-review"]

CONTENT = """
# Troubleshooting Guide

## Overview

Effective troubleshooting follows a systematic approach:
1. Understand the problem
2. Reproduce the issue
3. Isolate the cause
4. Apply a fix
5. Verify the solution

## General Troubleshooting Process

### Step 1: Gather Information

**Ask these questions:**
- What is the expected behavior?
- What is the actual behavior?
- When did the problem start?
- What changed recently?
- Is it reproducible?

**Collect these details:**
- Error messages (full text)
- Stack traces
- Log entries
- Environment details
- Steps to reproduce

### Step 2: Reproduce the Issue

**Why reproduction matters:**
- Confirms understanding of the problem
- Allows testing of fixes
- Helps identify root cause

**Reproduction checklist:**
- [ ] Same environment (OS, version, configuration)
- [ ] Same data/inputs
- [ ] Same sequence of actions
- [ ] Minimal reproduction case

### Step 3: Isolate the Cause

**Binary search approach:**
```
1. Does it work in production but not locally?
   -> Environment difference

2. Does it work with old code but not new?
   -> Recent change (use git bisect)

3. Does it work with different data?
   -> Data-specific issue

4. Does it work in isolation?
   -> Integration/dependency issue
```

### Step 4: Apply Fix

**Before fixing:**
- Understand why it's broken
- Consider side effects
- Write a test for the issue

**Fix approach:**
- Make minimal changes
- Fix root cause, not symptoms
- Document the fix

### Step 5: Verify Solution

- [ ] Original issue resolved
- [ ] No new issues introduced
- [ ] Tests pass
- [ ] Works in target environment

## Common Issue Categories

### Build/Compilation Errors

**Symptoms:**
- Build fails
- Compilation errors
- Module not found

**Common causes:**
- Missing dependencies
- Version mismatches
- Incorrect configuration
- Syntax errors

**Solutions:**

```bash
# Clear caches and reinstall
rm -rf node_modules package-lock.json
npm install

# Python virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Check versions
node --version
python --version
```

### Runtime Errors

**Symptoms:**
- Crashes
- Exceptions
- Unexpected behavior

**Debugging approach:**

```python
# Add logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def problematic_function(data):
    logger.debug(f"Input data: {data}")
    # ... function logic
    logger.debug(f"Output: {result}")
    return result
```

```javascript
// Browser debugging
console.log('Variable state:', variable);
debugger; // Pause execution

// Node.js debugging
node --inspect script.js
```

### Performance Issues

**Symptoms:**
- Slow response times
- High CPU/memory usage
- Timeouts

**Profiling tools:**

```python
# Python profiling
import cProfile
cProfile.run('function_to_profile()')

# Memory profiling
from memory_profiler import profile
@profile
def memory_intensive_function():
    pass
```

```bash
# System-level profiling
top -p <pid>
htop
```

**Common causes:**
- N+1 queries
- Missing indexes
- Memory leaks
- Synchronous blocking
- Inefficient algorithms

### Database Issues

**Connection problems:**
```bash
# Test connection
psql -h localhost -U user -d database

# Check if service is running
sudo systemctl status postgresql

# Check port
netstat -tlnp | grep 5432
```

**Query problems:**
```sql
-- Explain query plan
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';

-- Check for missing indexes
SELECT * FROM pg_stat_user_indexes WHERE idx_scan = 0;
```

### Network Issues

**Connectivity checks:**
```bash
# Test endpoint
curl -v https://api.example.com/health

# DNS resolution
nslookup api.example.com

# Port connectivity
telnet api.example.com 443
nc -zv api.example.com 443

# Trace route
traceroute api.example.com
```

**Common causes:**
- DNS issues
- Firewall rules
- SSL/TLS certificate problems
- Proxy configuration
- Timeout settings

### Authentication/Authorization Issues

**Debugging steps:**
1. Verify credentials are correct
2. Check token expiration
3. Verify permissions/roles
4. Check request headers
5. Review auth logs

```bash
# Decode JWT token
echo "token" | cut -d'.' -f2 | base64 -d | jq

# Check token expiration
jwt decode <token>
```

### Environment Issues

**"Works on my machine" problems:**

```bash
# Compare environments
diff <(env | sort) <(ssh prod "env | sort")

# Check versions
python --version
node --version
docker --version

# Check environment variables
printenv | grep -i database
```

**Docker-specific:**
```bash
# View logs
docker logs container_name

# Enter container
docker exec -it container_name /bin/sh

# Check networking
docker network inspect bridge
```

## Debugging Tools

### Logging Best Practices

```python
import logging

# Configure structured logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Log levels usage
logging.debug("Detailed info for debugging")
logging.info("General operational info")
logging.warning("Something unexpected happened")
logging.error("Error occurred, but app continues")
logging.critical("Severe error, app may crash")
```

### Using Git Bisect

Find the commit that introduced a bug:

```bash
# Start bisect
git bisect start

# Mark current version as bad
git bisect bad

# Mark known good version
git bisect good v1.0.0

# Git will checkout commits to test
# After testing each:
git bisect good  # or
git bisect bad

# Find the culprit commit
# Reset when done
git bisect reset
```

### Remote Debugging

```python
# Python remote debugging with debugpy
import debugpy
debugpy.listen(5678)
debugpy.wait_for_client()
```

```javascript
// Node.js remote debugging
node --inspect=0.0.0.0:9229 app.js
```

## Issue-Specific Guides

### "Module Not Found" Errors

```bash
# Check if installed
pip list | grep package_name
npm list package_name

# Check import path
python -c "import sys; print(sys.path)"

# Reinstall
pip install --force-reinstall package_name
npm install package_name
```

### "Permission Denied" Errors

```bash
# Check file permissions
ls -la file_name

# Check ownership
stat file_name

# Fix permissions
chmod 644 file_name
chown user:group file_name
```

### Memory Leaks

**Identification:**
```bash
# Monitor memory over time
watch -n 1 'ps -o pid,rss,command -p <pid>'
```

**Common causes:**
- Event listener not removed
- Circular references
- Global caches without limits
- Closures holding references

### SSL/TLS Certificate Issues

```bash
# Check certificate
openssl s_client -connect example.com:443

# Verify certificate chain
openssl verify -CAfile ca.pem server.pem

# Check expiration
openssl x509 -enddate -noout -in cert.pem
```

## Escalation Process

### When to Escalate

- Issue affects production
- Security vulnerability discovered
- Unable to resolve after reasonable effort
- Issue requires access you don't have

### How to Escalate

**Include in escalation:**
1. Clear problem description
2. Steps already taken
3. Current hypothesis
4. Evidence collected
5. Urgency/impact assessment

### Incident Documentation

```markdown
## Incident Report

**Date:** 2024-01-15
**Severity:** High
**Status:** Resolved

### Summary
Brief description of the incident.

### Timeline
- 10:00 - Issue reported
- 10:15 - Investigation started
- 10:45 - Root cause identified
- 11:00 - Fix deployed
- 11:15 - Issue resolved

### Root Cause
Detailed explanation of what caused the issue.

### Resolution
Steps taken to resolve the issue.

### Prevention
Actions to prevent recurrence.
```

## Prevention

### Proactive Monitoring

Set up alerts for:
- Error rate spikes
- Response time degradation
- Resource utilization
- Failed health checks

### Regular Maintenance

- Update dependencies
- Review logs periodically
- Test backup/restore
- Rotate credentials
- Clean up temporary data

---

*This guide complements your project's logging and monitoring setup*
"""
