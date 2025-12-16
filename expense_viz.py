import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = 'expenses.csv'

def load_data():
    """
    載入 expenses.csv 資料。
    """
    if not os.path.exists(FILE_NAME):
        print(f"錯誤：找不到 '{FILE_NAME}' 檔案。請先執行輸入模組產生數據。")
        return None
    
    try:
        # 使用 pandas 讀取 CSV 檔案
        df = pd.read_csv(FILE_NAME)
        return df
    except Exception as e:
        print(f"讀取資料失敗: {e}")
        return None

def generate_pie_chart(df):
    """
    根據 'Category' 欄位生成圓餅圖。
    """
    if df.empty:
        print("資料為空，無法生成圖表。")
        return

    # 1. 計算每個類別的總金額
    category_summary = df.groupby('Category')['Amount'].sum()

    # 2. 繪製圓餅圖
    plt.figure(figsize=(8, 8))
    
    # autopct='%1.1f%%' 顯示百分比
    plt.pie(
        category_summary, 
        labels=category_summary.index, 
        autopct='%1.1f%%', 
        startangle=90
    )
    plt.title('Expense Distribution by Category')
    plt.axis('equal')  # 確保圓餅圖是圓形的
    
    # 3. 顯示圖表
    plt.tight_layout()
    plt.savefig("pie_chart.png", dpi=200)
    print("已輸出圖表：pie_chart.png")

def main():
    print("--- 啟動費用視覺化模組 ---")
    data = load_data()
    
    if data is not None and not data.empty:
        generate_pie_chart(data)
    elif data is not None:
        print("資料已載入，但表格是空的。")

if __name__ == "__main__":
    # 確保安裝依賴庫 (如果尚未安裝)
    # 可以在 Terminal 中執行： pip install pandas matplotlib
    main()                                                                              