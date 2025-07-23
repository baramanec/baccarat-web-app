from collections import Counter

def predict_next_bet(trend):
    if not trend:
        return '無法預測', 0.0

    counts = Counter(trend.upper())
    total = sum(counts.get(c, 0) for c in 'BP')

    if total == 0:
        return '無法預測', 0.0

    b_rate = counts.get('B', 0) / total
    p_rate = counts.get('P', 0) / total

    if b_rate > p_rate:
        return '莊', b_rate
    elif p_rate > b_rate:
        return '閒', p_rate
    else:
        return '觀望', 0.5