# core/guides/deployment_guide.py
# Deployment Guide (v3.2.0)

"""
Deployment Guide.

Provides comprehensive instructions for deploying the application
to various environments.

Introduced in v3.2.0.
"""

GUIDE_ID = "deployment-guide"

GUIDE = {
    "title": "Deployment Guide",
    "purpose": "Document deployment procedures and best practices",
    "audience": "DevOps engineers and developers",
    "complexity": "intermediate",
}

RELATED_PRINCIPLES = ["ci-workflow", "versioning", "security"]

CONTENT = """
# Deployment Guide

## Purpose

This guide documents the procedures for deploying the application to
different environments, including prerequisites, step-by-step instructions,
and rollback procedures.

## Environments

| Environment | Purpose | URL |
|-------------|---------|-----|
| Development | Local development | localhost:3000 |
| Staging | Pre-production testing | staging.example.com |
| Production | Live environment | app.example.com |

## Prerequisites

### Required Tools

```bash
# Docker
docker --version  # 20.x+
docker-compose --version  # 2.x+

# Kubernetes (if applicable)
kubectl version
helm version  # 3.x+

# Cloud CLI (choose one)
aws --version    # AWS
gcloud version   # GCP
az --version     # Azure
```

### Access Requirements

- [ ] VPN access (if required)
- [ ] Container registry credentials
- [ ] Cloud provider credentials
- [ ] SSH keys for servers
- [ ] Database credentials
- [ ] Secrets management access

## Local Development

### Docker Compose Setup

```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f app

# Stop services
docker-compose down
```

### Environment Variables

```bash
# Copy example environment file
cp .env.example .env

# Edit with your local settings
# Required variables:
DATABASE_URL=postgresql://user:pass@localhost:5432/app
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key
```

## Build Process

### Application Build

```bash
# Install dependencies
npm install  # or pip install -r requirements.txt

# Run tests
npm test

# Build for production
npm run build

# Verify build output
ls -la dist/
```

### Docker Build

```bash
# Build image
docker build -t app:latest .

# Build with specific tag
docker build -t app:$(git rev-parse --short HEAD) .

# Multi-stage build for smaller images
docker build --target production -t app:prod .
```

### Container Registry

```bash
# Login to registry
docker login registry.example.com

# Tag for registry
docker tag app:latest registry.example.com/app:latest
docker tag app:latest registry.example.com/app:$(git rev-parse --short HEAD)

# Push to registry
docker push registry.example.com/app:latest
docker push registry.example.com/app:$(git rev-parse --short HEAD)
```

## Deployment Procedures

### Staging Deployment

**Automated (CI/CD):**
1. Push to `develop` branch
2. CI pipeline runs tests
3. Successful tests trigger staging deployment
4. Slack notification sent

**Manual:**
```bash
# Connect to staging
ssh deploy@staging.example.com

# Pull latest image
docker pull registry.example.com/app:latest

# Update service
docker-compose -f docker-compose.staging.yml up -d

# Verify deployment
docker-compose ps
curl -f http://localhost:3000/health
```

### Production Deployment

**Pre-deployment Checklist:**
- [ ] All tests pass
- [ ] Staging verification complete
- [ ] Database migrations tested
- [ ] Rollback plan documented
- [ ] Team notified
- [ ] Monitoring dashboards open

**Deployment Steps:**

1. **Create deployment tag:**
   ```bash
   git tag -a v1.2.3 -m "Release v1.2.3"
   git push origin v1.2.3
   ```

2. **Run database migrations:**
   ```bash
   # Backup database first
   pg_dump -h prod-db -U app app > backup_$(date +%Y%m%d).sql

   # Run migrations
   npm run migrate:prod
   ```

3. **Deploy application:**
   ```bash
   # Blue-green deployment
   kubectl set image deployment/app app=registry.example.com/app:v1.2.3

   # Monitor rollout
   kubectl rollout status deployment/app

   # Verify
   kubectl get pods
   ```

4. **Post-deployment verification:**
   ```bash
   # Health check
   curl -f https://app.example.com/health

   # Smoke tests
   npm run test:smoke:prod

   # Monitor error rates
   # Check monitoring dashboard
   ```

### Kubernetes Deployment

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: app
        image: registry.example.com/app:latest
        ports:
        - containerPort: 3000
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        readinessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 10
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 15
          periodSeconds: 20
```

**Apply deployment:**
```bash
# Apply configuration
kubectl apply -f deployment.yaml

# Scale if needed
kubectl scale deployment/app --replicas=5

# Check status
kubectl get deployments
kubectl describe deployment app
```

## Database Migrations

### Migration Best Practices

1. **Always backup before migrating**
2. **Test migrations on staging first**
3. **Make migrations reversible when possible**
4. **Run during low-traffic periods**

### Running Migrations

```bash
# Check pending migrations
npm run migrate:status

# Run migrations
npm run migrate:up

# Rollback if needed
npm run migrate:down
```

### Zero-Downtime Migrations

For large tables or complex changes:

1. **Add new column (nullable)**
2. **Deploy code that writes to both columns**
3. **Backfill data**
4. **Deploy code that reads from new column**
5. **Remove old column**

## Rollback Procedures

### Application Rollback

```bash
# Kubernetes
kubectl rollout undo deployment/app

# Docker Compose
docker-compose pull  # pulls previous image
docker-compose up -d

# Check rollback status
kubectl rollout history deployment/app
```

### Database Rollback

```bash
# Run rollback migration
npm run migrate:down

# Or restore from backup
psql -h prod-db -U app app < backup_20240115.sql
```

### Emergency Procedures

1. **Immediate rollback:** Revert to previous version
2. **Notify team:** Alert via Slack/PagerDuty
3. **Investigate:** Check logs and monitoring
4. **Post-mortem:** Document what went wrong

## Monitoring and Verification

### Health Checks

```bash
# Basic health
curl -f https://app.example.com/health

# Detailed health
curl https://app.example.com/health/detailed

# Expected response
{
  "status": "healthy",
  "version": "1.2.3",
  "database": "connected",
  "cache": "connected"
}
```

### Log Monitoring

```bash
# Kubernetes logs
kubectl logs -f deployment/app

# Docker logs
docker-compose logs -f app

# Aggregate logs (if configured)
# Check Datadog/Splunk/ELK
```

### Key Metrics to Watch

- **Error rate:** Should remain below 0.1%
- **Response time:** p99 < 500ms
- **CPU/Memory:** Below 80% utilization
- **Request rate:** Compare to baseline

## Configuration Management

### Environment-Specific Config

```yaml
# config/production.yaml
database:
  host: prod-db.example.com
  pool_size: 20
  ssl: true

cache:
  host: prod-cache.example.com
  ttl: 3600

logging:
  level: INFO
  format: json
```

### Secrets Management

```bash
# Kubernetes secrets
kubectl create secret generic app-secrets \\
  --from-literal=DATABASE_URL=postgresql://... \\
  --from-literal=API_KEY=...

# AWS Secrets Manager
aws secretsmanager get-secret-value --secret-id app/production

# HashiCorp Vault
vault kv get secret/app/production
```

## Troubleshooting

### Common Issues

**Container won't start:**
```bash
# Check logs
docker logs container_name

# Check resources
docker stats

# Verify image
docker inspect image_name
```

**Database connection fails:**
```bash
# Test connectivity
psql -h hostname -U user -d database

# Check connection string
echo $DATABASE_URL

# Verify network/firewall
telnet hostname 5432
```

**High memory usage:**
```bash
# Check container stats
docker stats

# Restart with limits
docker-compose up -d --scale app=2
```

### Getting Help

1. Check monitoring dashboards
2. Review recent deployments
3. Search error messages in logs
4. Escalate to on-call engineer
5. Document in incident report

## Security Considerations

- Never commit secrets to version control
- Rotate credentials regularly
- Use least-privilege access
- Encrypt data in transit and at rest
- Audit deployment access

---

*Update this guide when deployment procedures change.*
"""
