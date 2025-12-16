import csv
import os
from datetime import datetime

FILE_NAME = 'expenses.csv'
FIELD_NAMES = ['Date', 'Amount', 'Category', 'Notes']

def initialize_csv():
    """
    檢查 CSV 檔案是否存在，如果不存在，則建立檔案並寫入標題 (Header)。
    """
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
            writer.writeheader()
        print(f"'{FILE_NAME}' 檔案已建立並寫入標題。")
    else:
        print(f"'{FILE_NAME}' 檔案已存在，將追加資料。")

def get_valid_input(prompt, data_type=str, validator=None):
    """
    通用輸入函數：確保使用者輸入有效。
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input and data_type != str:
            print("此欄位不能為空。")
            continue
        try:
            # 類型檢查
            if data_type == float:
                value = float(user_input)
            elif data_type == str:
                value = user_input
            else:
                value = user_input # 預設字串

            # 額外驗證 (例如日期格式)
            if validator and not validator(value):
                print("輸入格式或數值無效，請重新輸入。")
                continue
            
            return value

        except ValueError:
            print(f"輸入格式錯誤，請輸入有效的 {data_type.__name__}。")

def validate_date(date_str):
    """驗證日期格式是否為 YYYY-MM-DD"""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def add_expense():
    """
    收集單筆費用資料。
    """
    print("\n--- 新增費用紀錄 ---")
    
    # 1. 日期 (必須輸入且格式正確)
    date_input = get_valid_input(
        "日期 (YYYY-MM-DD): ", 
        data_type=str, 
        validator=validate_date
    )
    
    # 2. 金額 (必須輸入且為有效數字)
    amount_input = get_valid_input(
        "金額 (數字): ", 
        data_type=float
    )
    
    # 3. 類別 (必須輸入)
    category_input = get_valid_input(
        "類別 (如：Food, Transport): ", 
        data_type=str
    )

    # 4. 備註 (可選)
    notes_input = input("備註 (可選，按 Enter 跳過): ").strip()
    
    new_expense = {
        'Date': date_input,
        'Amount': amount_input,
        'Category': category_input,
        'Notes': notes_input
    }
    
    return new_expense

def save_expense(expense_data):
    """
    將單筆費用資料追加寫入 CSV 檔案。
    """
    try:
        with open(FILE_NAME, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
            writer.writerow(expense_data)
        print("✅ 紀錄儲存成功！")
    except Exception as e:
        print(f"❌ 儲存失敗: {e}")

def main():
    initialize_csv() # 確保檔案存在且有標題
    
    while True:
        expense = add_expense()
        save_expense(expense)
        
        # 詢問是否繼續
        if input("\n是否繼續新增費用? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()