"""第 57 批：技能冷却在充能类技能上越用越快：冷却按真实时间累..."""


def scaled_time(dt, time_scale):
    """按时间缩放推进冷却。"""
    return dt * time_scale


def charge_fraction(current, per_charge):
    """返回充能进度。"""
    if per_charge <= 0:
        return 0.0
    return min(current / per_charge, 1.0)


def cooldown_reduction(base, reductions):
    """按加法计算冷却缩减。"""
    return max(base - sum(reductions), 0.0)


def refund_on_fail(remaining, cost):
    """释放失败时返还冷却。"""
    return remaining + cost


def segment_key(skill_id, segment):
    """返回多段技能冷却键。"""
    return (skill_id, segment)


def restore_event(count, amount):
    """逐次恢复充能。"""
    return count + amount


def server_remaining(client, latency):
    """按延迟校正服务器剩余冷却。"""
    return max(client - latency, 0.0)


def death_scale(is_dead):
    """死亡时暂停冷却。"""
    return 0.0 if is_dead else 1.0


def weapon_key(weapon_id, skill_id):
    """按武器隔离冷却。"""
    return (weapon_id, skill_id)


def fixed_step(dt, step):
    """返回统一时间步。"""
    if step <= 0:
        return 0.0
    return (dt // step) * step
