# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for building some python packages if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
# Note: We'll create requirements.txt in next step
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create directory for agents/database
RUN mkdir -p .agents && chmod 777 .agents

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV KAIZEN_ENV=production

# Run the core agent
CMD ["python", "-m", "kaizen_core.main"]
