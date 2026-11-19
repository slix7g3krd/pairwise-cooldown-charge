"""第 57 批：技能冷却在充能类技能上越用越快：冷却按真实时间累..."""

def scaled_time(dt, time_scale):
    """按时间缩放推进冷却。"""
    raise NotImplementedError("TODO: scaled_time")

def charge_fraction(current, per_charge):
    """返回充能进度。"""
    raise NotImplementedError("TODO: charge_fraction")

def cooldown_reduction(base, reductions):
    """按加法计算冷却缩减。"""
    raise NotImplementedError("TODO: cooldown_reduction")

def refund_on_fail(remaining, cost):
    """释放失败时返还冷却。"""
    raise NotImplementedError("TODO: refund_on_fail")

def segment_key(skill_id, segment):
    """返回多段技能冷却键。"""
    raise NotImplementedError("TODO: segment_key")

def restore_event(count, amount):
    """逐次恢复充能。"""
    raise NotImplementedError("TODO: restore_event")

def server_remaining(client, latency):
    """按延迟校正服务器剩余冷却。"""
    raise NotImplementedError("TODO: server_remaining")

def death_scale(is_dead):
    """死亡时暂停冷却。"""
    raise NotImplementedError("TODO: death_scale")

def weapon_key(weapon_id, skill_id):
    """按武器隔离冷却。"""
    raise NotImplementedError("TODO: weapon_key")

def fixed_step(dt, step):
    """返回统一时间步。"""
    raise NotImplementedError("TODO: fixed_step")
