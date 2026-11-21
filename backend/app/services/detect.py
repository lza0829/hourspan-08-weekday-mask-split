from app.modules import weekday_mask_split


def run_detect(batch_id: str | None = None):
    """变更检测走 weekday_mask_split：以现行有效段为基准，mask 任一 bit 变化即计变更。"""
    return weekday_mask_split.run_detect(batch_id)
