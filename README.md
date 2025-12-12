# 🚀 VNUK 2025: Selenium Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium)
![Pattern](https://img.shields.io/badge/Design%20Pattern-POM-orange?style=for-the-badge)

> Dự án kiểm thử tự động hóa cho ứng dụng web Railway, được xây dựng dựa trên Selenium WebDriver và Python. Dự án áp dụng mô hình **Page Object Model (POM)** và **Dynamic Data Generation** để đảm bảo tính ổn định và bảo trì.

---

## 📂 Cấu trúc Dự án

Dự án được tổ chức theo mô-đun chuyên nghiệp:

```text
selenium-python-example/
├── 📂 base/                 # Lớp cơ sở (Base Page)
│   └── 🐍 base_page.py      # Xử lý các hành động chung (Wait, Click, Scroll)
├── 📂 pages/                # Page Objects (POM)
│   ├── 🐍 login_page.py     # Trang Đăng nhập
│   ├── 🐍 register_page.py  # Trang Đăng ký
│   ├── 🐍 book_ticket_page.py # Trang Đặt vé
│   └── 🐍 home_page.py      # Trang Chủ
├── 📂 test/                 # Chứa các Test Case
│   ├── 🐍 test_flows.py     # Luồng kiểm thử chính (End-to-End)
│   └── 🐍 test_login.py     # Test đăng nhập cơ bản
└── 📝 README.md             # Tài liệu dự án
````

-----

## 🛠️ Cài đặt & Yêu cầu

### Tiền điều kiện

  * **Python 3.x**
  * **Google Chrome** trình duyệt mới nhất
  * **Thư viện Selenium:**
    ```bash
    pip install selenium
    ```

-----

## ⚡ Hướng dẫn chạy Test

Do cấu trúc dự án đã phân chia module, bạn cần chạy lệnh từ thư mục gốc như sau:

| Mục tiêu | Lệnh thực thi (Terminal) |
| :--- | :--- |
| **Chạy luồng chính (Full Flow)** | `python -m test.test_flows` |
| **Chạy luồng Login cơ bản** | `python -m test.test_login` |

> **Lưu ý:** Không chạy trực tiếp bằng `python test/test_flows.py` để tránh lỗi import module.

-----

## 🧩 Chi tiết Kịch bản (Test Scenarios)

### `test_flows.py` (End-to-End Testing)

Kịch bản này kiểm thử toàn bộ luồng người dùng thực tế:

| Bước | Hành động | Chi tiết kỹ thuật |
| :--- | :--- | :--- |
| **1** | **Tạo dữ liệu** | Tự động sinh Email và CMND/PID ngẫu nhiên (tránh lỗi trùng lặp). |
| **2** | **Đăng ký** | Truy cập trang Register -\> Tạo tài khoản mới. |
| **3** | **Đăng nhập** | Dùng tài khoản vừa tạo để Login vào hệ thống. |
| **4** | **Đặt vé** | Chọn ga đi ga đến phù hợp, loại ghế và đặt vé. |
| **5** | **Xác thực** | Kiểm tra thông báo *"Ticket booked successfully\!"* xuất hiện. |

-----

## ⚙️ Các tính năng nổi bật

  * **Dynamic Data:** Sử dụng hàm random để tạo Email/PID mới mỗi lần chạy -\> Test không bao giờ chết vì dữ liệu cũ.
  * **Explicit Waits:** Sử dụng `WebDriverWait` trong `BasePage` thay vì `sleep()` cứng -\> Tăng tốc độ chạy test.
  * **Auto-Scroll:** Tự động cuộn tới phần tử trước khi click -\> Tránh lỗi element not visible.
  * **Error Handling:** Tự động in ra danh sách lựa chọn trong Dropdown nếu không tìm thấy giá trị (hỗ trợ Debug).

-----

## 🛣️ Roadmap & Trạng thái

  - [x] ✅ Thay thế `sleep()` bằng `WebDriverWait`.
  - [x] ✅ Hỗ trợ đầy đủ luồng: Register -\> Login -\> Book Ticket.
  - [x] ✅ Xử lý dữ liệu động (Random Data).
  - [x] ✅ Thêm Screenshot khi test thất bại.
  - [ ] 📄 Thêm file config để quản lý URL và Browser.
  - [ ] 📊 Xuất báo cáo HTML (HTML Reporting).

-----

*© 2025 VNUK Automation Project*
