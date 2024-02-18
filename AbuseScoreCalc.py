# Define weights for each metric (you can adjust these)
weight_glance_views = 0.2
weight_search_impressions = 0.3
weight_gms = 0.3
weight_return_rate = 0.2

# Define thresholds for abuse detection (you can adjust these)
threshold_glance_views = 1000
threshold_search_impressions = 5000
threshold_gms = 10000
threshold_return_rate = 0.1  # 10% return ratepy

# Sample data for ASIN in T4W
glance_views = 1200
search_impressions = 6000
gms = 9000
return_rate = 0.12  # 12% return rate

# Calculate the ASIN abuse score
abuse_score = (
    (glance_views / threshold_glance_views) * weight_glance_views +
    (search_impressions / threshold_search_impressions) * weight_search_impressions +
    (gms / threshold_gms) * weight_gms +
    ((1 - return_rate) / (1 - threshold_return_rate)) * weight_return_rate
)

print(f'ASIN Abuse Score: {abuse_score:.2f}')
