#!/bin/bash
# validate-pipeline.sh — Check pipeline health
# Identifies stale artifacts, missing phases, and pipeline bottlenecks
#
# Usage: ./scripts/validate-pipeline.sh [base-dir]

set -e

BASE_DIR="${1:-.}"
NOW=$(date +%s)
WARN_DAYS=7
OVERDUE_DAYS=14

echo "Git for Strategy — Pipeline Health Check"
echo "=========================================="
echo ""

# Check each phase directory
check_phase() {
    local phase="$1"
    local dir="$2"
    local next_phase="$3"
    
    if [ ! -d "$BASE_DIR/$dir" ]; then
        echo "  ⚪ $phase: No directory (run init-strategy.sh first)"
        return
    fi
    
    local count=$(find "$BASE_DIR/$dir" -name "*.md" -type f 2>/dev/null | wc -l)
    
    if [ "$count" -eq 0 ]; then
        echo "  ⚪ $phase: Empty — no artifacts yet"
        return
    fi
    
    # Find most recent file
    local newest=$(find "$BASE_DIR/$dir" -name "*.md" -type f -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1)
    local newest_time=$(echo "$newest" | cut -d' ' -f1 | cut -d'.' -f1)
    local newest_file=$(echo "$newest" | cut -d' ' -f2-)
    local age_days=$(( (NOW - newest_time) / 86400 ))
    
    if [ "$age_days" -gt "$OVERDUE_DAYS" ]; then
        echo "  ⚪ $phase: $count artifacts, newest is ${age_days}d old (OVERDUE)"
    elif [ "$age_days" -gt "$WARN_DAYS" ]; then
        echo "  ⚪ $phase: $count artifacts, newest is ${age_days}d old (getting stale)"
    else
        echo "  ⚪ $phase: $count artifacts, newest is ${age_days}d old"
    fi
    echo "     Latest: $(basename "$newest_file")"
}

check_phase "Explore"  "scouts"       "Decide"
check_phase "Decide"   "specs"        "Execute"
check_phase "Execute"  "commissions"  "Learn"
check_phase "Learn"    "retros"       "Explore"

echo ""

# Check STATUS.md
if [ -f "$BASE_DIR/STATUS.md" ]; then
    local_status_age=$(( (NOW - $(stat -c %Y "$BASE_DIR/STATUS.md" 2>/dev/null || echo $NOW)) / 86400 ))
    if [ "$local_status_age" -gt "$WARN_DAYS" ]; then
        echo "STATUS.md is ${local_status_age}d old — consider running /status"
    else
        echo "STATUS.md is current (${local_status_age}d old)"
    fi
else
    echo "No STATUS.md found — run /status to create one"
fi

# Check seeds
seed_count=$(find "$BASE_DIR/../seeds" -name "*.md" -not -name "README.md" -type f 2>/dev/null | wc -l)
echo "$seed_count seed patches available"

echo ""
echo "Done. Run /status for a detailed update."
