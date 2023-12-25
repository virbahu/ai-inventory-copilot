import numpy as np
def calculate_inv_copilot_query(query, sku_data):
    inv = sku_data.get("on_hand", 0)
    demand = sku_data.get("daily_demand", 10)
    lt = sku_data.get("lead_time", 7)
    dos = inv / max(demand, 0.01)
    ss = 1.645 * sku_data.get("demand_std", demand*0.2) * (lt**0.5)
    rop = demand * lt + ss
    action = "reorder_now" if inv <= rop else "monitor" if inv <= rop * 1.3 else "healthy"
    return {"sku": sku_data.get("sku","?"), "days_of_stock": round(dos,1), "safety_stock": round(ss,0), "reorder_point": round(rop,0), "status": action}
if __name__=="__main__":
    print(calculate_inv_copilot_query("check stock", {"sku":"A1","on_hand":80,"daily_demand":15,"demand_std":4,"lead_time":7}))
