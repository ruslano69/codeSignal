def pressureGauges(morning, evening):
    return [[min(x) for x in zip(morning,evening)],[max(x) for x in zip(morning,evening)]]
