#!/usr/bin/env python3
"""
Amazon FBA Cross-Border Seller Stack TCO Calculator 2026.
Combines Helium 10 (ERP) + AdsPower (Storefront Isolation) + Firstbase.io (US LLC & Tax).
"""
import argparse

def calculate(stores, revenue):
    # Helium 10 Platinum Annual: $79/mo ($948/yr)
    h10_monthly = 79.0

    # AdsPower: Base 50 profiles $19/mo (plenty for multiple Amazon accounts & email setups)
    adspower_monthly = 19.0

    # Firstbase.io: $399 one-time setup amortized ($33.25/mo) + $99/yr registered agent ($8.25/mo) = $41.50/mo
    firstbase_monthly = 41.50

    total_monthly = h10_monthly + adspower_monthly + firstbase_monthly
    annual_total = total_monthly * 12.0

    print("=" * 65)
    print("Cross-Border Amazon FBA Merchant Infrastructure Budget 2026")
    print("=" * 65)
    print(f"1. Product ERP & Analytics (Helium 10):  ${h10_monthly:.2f}/mo ($948.00/yr)")
    print(f"2. Anti-Detect Browser (AdsPower 50p):   ${adspower_monthly:.2f}/mo ($228.00/yr)")
    print(f"3. US Corporate & Tax (Firstbase.io):    ${firstbase_monthly:.2f}/mo ($498.00/yr)")
    print("-" * 65)
    print(f"Total Monthly Operating Infrastructure:  ${total_monthly:.2f}/mo")
    print(f"Total Annual Merchant Infrastructure:    ${annual_total:,.2f}/yr")
    print("=" * 65)
    return total_monthly

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crossborder Seller Stack Calculator")
    parser.add_argument("--stores", type=int, default=2)
    parser.add_argument("--revenue", type=float, default=150000.0)
    args = parser.parse_args()
    calculate(args.stores, args.revenue)
