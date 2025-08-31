#!/bin/bash

# FMP Symbol Sync Setup Script
# This script helps set up the FMP Symbol Sync DAG

echo "FMP Symbol Sync Setup"
echo "===================="

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ Created .env file. Please edit it with your FMP API key."
    echo ""
    echo "To get an FMP API key:"
    echo "1. Visit https://financialmodelingprep.com/"
    echo "2. Sign up for an account"
    echo "3. Get your API key from the dashboard"
    echo "4. Edit .env file and set FMP_API_KEY=your_api_key"
    echo ""
else
    echo "✓ .env file already exists"
fi

# Check if FMP_API_KEY is set
source .env 2>/dev/null
if [ -z "$FMP_API_KEY" ] || [ "$FMP_API_KEY" = "your_fmp_api_key_here" ]; then
    echo "⚠  FMP_API_KEY not set in .env file"
    echo "   Please edit .env and set your actual API key"
else
    echo "✓ FMP_API_KEY is configured"
fi

# Check if Docker is running
if ! docker info >/dev/null 2>&1; then
    echo "✗ Docker is not running. Please start Docker first."
    exit 1
else
    echo "✓ Docker is running"
fi

# Check if containers are running
if docker-compose ps | grep -q "Up"; then
    echo "✓ Airflow containers are running"
    echo ""
    echo "You can access Airflow at: http://localhost:8080"
    echo "Username: airflow"
    echo "Password: airflow"
    echo ""
    echo "The FMP Symbol Sync DAG should be available in the DAGs list."
else
    echo "⚠  Airflow containers are not running"
    echo ""
    echo "To start Airflow:"
    echo "  docker-compose up -d"
    echo ""
    echo "To view logs:"
    echo "  docker-compose logs -f"
    echo ""
    echo "To stop Airflow:"
    echo "  docker-compose down"
fi

echo ""
echo "Next steps:"
echo "1. Ensure FMP_API_KEY is set in .env file"
echo "2. Start Airflow: docker-compose up -d"
echo "3. Access UI: http://localhost:8080"
echo "4. Enable the 'fmp_symbol_sync' DAG"
echo "5. Trigger a test run"
echo ""
echo "For troubleshooting, see FMP_SYMBOL_SYNC_SETUP.md"
