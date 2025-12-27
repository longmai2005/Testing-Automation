```markdown
# 🚂 Railway Automation Testing Framework

Dự án kiểm thử tự động (Automation Testing) cho hệ thống **Railway Booking** (`http://railwayb1.somee.com`).
Dự án được xây dựng bằng **Python**, **Selenium WebDriver**, **Pytest** và sử dụng **Allure Report** để xuất báo cáo chuyên nghiệp.

---

## 🛠 Yêu cầu hệ thống (Prerequisites)

Trước khi bắt đầu, hãy đảm bảo máy tính của bạn đã cài đặt:

1.  **Python 3.10+**
2.  **Google Chrome**: Phiên bản mới nhất.
3.  **Java (JDK 8+)**: Cần thiết để chạy Allure Commandline. 

---

## ⚙️ Hướng dẫn Cài đặt (Installation)

### Bước 1: Clone dự án và tạo môi trường ảo (Virtual Environment)

Mở Terminal (Mac) hoặc CMD/PowerShell (Windows) tại thư mục dự án:

**MacOS / Linux:**
```bash
# Tạo môi trường ảo
python3 -m venv venv

# Kích hoạt môi trường (Bắt buộc mỗi khi mở lại terminal)
source venv/bin/activate

```

**Windows:**

```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường
.\venv\Scripts\activate

```

### Bước 2: Cài đặt thư viện Python

```bash
pip install -r requirements.txt

```

### Bước 3: Cài đặt Allure Commandline (Bắt buộc để xem báo cáo)

Bạn cần cài công cụ Allure vào máy tính (System Path) thì mới xem được báo cáo.

**🍏 Đối với MacOS:**
Sử dụng Homebrew (Khuyên dùng):

```bash
brew install allure

```

*Nếu chưa có Homebrew, chạy lệnh này trước:*
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

**🪟 Đối với Windows:**
Cách 1: Sử dụng PowerShell (Nếu đã cài Scoop)

```powershell
scoop install allure

```

Cách 2: Tải thủ công

1. Tải file zip từ [Maven Central](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/).
2. Giải nén vào ổ C.
3. Thêm đường dẫn thư mục `bin` của Allure vào biến môi trường **PATH** của Windows.

**Cách chung (Nếu máy đã có Node.js):**

```bash
npm install -g allure-commandline

```

---

## 🚀 Hướng dẫn Chạy Test (Execution)

Đảm bảo bạn đã kích hoạt môi trường ảo (`source venv/bin/activate`) trước khi chạy.

### 1. Chạy toàn bộ Test Case

Lệnh này sẽ chạy tất cả các file test trong thư mục `tests/`:

```bash
python3 -m pytest --alluredir=allure-results

```

*(Trên Windows dùng `python` thay vì `python3`)*

### 2. Chạy riêng lẻ từng Module

Nếu bạn chỉ muốn test một chức năng cụ thể:

* **Test Đăng ký (Register):**
```bash
python3 -m pytest tests/test_03_register.py --alluredir=allure-results

```


* **Test Đăng nhập (Login):**
```bash
python3 -m pytest tests/test_02_auth.py --alluredir=allure-results

```


* **Test Đặt vé (Book Ticket):**
```bash
python3 -m pytest tests/test_04_book_ticket.py --alluredir=allure-results

```



### 3. Xem báo cáo kết quả (Allure Report)

Sau khi chạy test xong, dùng lệnh sau để mở báo cáo trên trình duyệt:

```bash
allure serve allure-results

```

*(Trình duyệt sẽ tự động mở trang web hiển thị biểu đồ kết quả Pass/Fail).*

---

## 📂 Cấu trúc dự án

```text
Railway_Automation/
├── tests/
│   ├── conftest.py             # Cấu hình Driver & Screenshot tự động
│   ├── test_01_general.py      # Test Home, FAQ, Link ngoài
│   ├── test_02_auth.py         # Test Login, Logout
│   ├── test_03_register.py     # Test Register (Validation, Alert)
│   ├── test_04_book_ticket.py  # Test Book Ticket (Logic nghiệp vụ)
│   └── test_05_manage.py       # Test My Ticket, Change Password
├── allure-results/             # Thư mục chứa dữ liệu báo cáo (JSON)
├── requirements.txt            # Danh sách thư viện cần thiết
└── README.md                   # Hướng dẫn sử dụng

```


---

**Author:** Mai Phước Long - 23020005
