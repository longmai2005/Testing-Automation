## 🚀 VNUK 2025: Selenium Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium)
![Pattern](https://img.shields.io/badge/Design%20Pattern-POM-orange?style=for-the-badge)

> Dự án kiểm thử tự động hóa cho ứng dụng web Railway, được xây dựng dựa trên Selenium WebDriver và Python. Dự án áp dụng mô hình **Page Object Model (POM)** và **Dynamic Data Generation** để đảm bảo tính ổn định và khả năng bảo trì cao.

---

## 📂 Cấu trúc Dự án (Project Structure)

Dự án được tổ chức theo cấu trúc mô-đun để dễ dàng mở rộng và quản lý:

```text
vnuk-2025/
├── 📂 base/                 # Lớp cơ sở (Base Page)
│   └── 🐍 base_page.py      # Xử lý các hành động chung (Wait, Click, Scroll)
├── 📂 pages/                # Page Objects (POM) - Chứa element và action của từng trang
│   ├── 🐍 login_page.py     
│   ├── 🐍 register_page.py  
│   ├── 🐍 book_ticket_page.py 
│   ├── 🐍 my_ticket_page.py
│   └── ...
├── 📂 test/                 # Chứa các Test Case (Kịch bản kiểm thử)
│   ├── 🐍 test_login.py     
│   ├── 🐍 test_book_ticket.py
│   ├── 🐍 test_flows.py     # Luồng kiểm thử End-to-End
│   └── ...
├── 📄 requirements.txt      # Các thư viện phụ thuộc
└── 📝 README.md             # Tài liệu dự án
````

-----

## 🛠️ Cài đặt & Yêu cầu (Installation)

### Tiền điều kiện

  * **Python 3.x** đã được cài đặt.
  * **Google Chrome** trình duyệt mới nhất.
  * **ChromeDriver** (Tương thích với bản Chrome hiện tại).

### Các bước cài đặt

1.  **Clone repository về máy:**

    ```bash
    git clone [https://bitbucket.org/agestvn/vnuk-2025](https://bitbucket.org/agestvn/vnuk-2025)
    cd vnuk-2025
    ```

2.  **Cài đặt các thư viện cần thiết:**

    ```bash
    pip install selenium
    ```

    *(Hoặc nếu có file requirements.txt)*: `pip install -r requirements.txt`

-----

## ⚡ Hướng dẫn chạy Test (Usage)

Để chạy kiểm thử, hãy đứng tại thư mục gốc của dự án và sử dụng lệnh module của Python:

| Mục tiêu | Lệnh thực thi (Terminal) |
| :--- | :--- |
| **Chạy toàn bộ test** | `python -m unittest discover test` |
| **Chạy luồng chính (Full Flow)** | `python -m test.test_flows` |
| **Chạy test Đăng nhập** | `python -m test.test_login` |
| **Chạy test Đặt vé** | `python -m test.test_book_ticket` |

> **Lưu ý:** Không chạy trực tiếp bằng `python test/test_login.py` để tránh lỗi import module. Hãy dùng `python -m ...`.

-----

## 🧩 Danh sách Test Case (Test Scenarios)

Dự án bao phủ các chức năng chính của hệ thống Railway:

| Module | Chức năng kiểm thử |
| :--- | :--- |
| **Register** | Đăng ký tài khoản mới, kiểm tra validate email/password, check trùng lặp. |
| **Login** | Đăng nhập thành công, đăng nhập sai pass, khóa tài khoản sau 5 lần sai. |
| **Book Ticket** | Đặt vé tàu, chọn ga đi/đến, chọn loại ghế, kiểm tra số lượng vé tối đa. |
| **My Ticket** | Xem vé đã đặt, Hủy vé (Cancel), Lọc vé (Filter). |
| **Flow** | Luồng End-to-End: Register -\> Login -\> Book Ticket -\> Verify -\> Logout. |

-----

## ⚙️ Các tính năng kỹ thuật nổi bật

  * **Page Object Model (POM):** Tách biệt code test và code xử lý giao diện, giúp code gọn gàng và dễ sửa chữa.
  * **Dynamic Data:** Sử dụng hàm random để tạo Email/PID mới mỗi lần chạy -\> Test không bao giờ chết vì dữ liệu cũ.
  * **Explicit Waits:** Sử dụng `WebDriverWait` thay vì `sleep()` cứng -\> Tăng tốc độ chạy test và độ ổn định.
  * **Javascript Executor:** Xử lý các trường hợp bị che khuất bởi quảng cáo hoặc UI phức tạp.
  * **Negative Testing:** Bao gồm cả các case kiểm thử lỗi (nhập sai data) để đảm bảo hệ thống chặn lỗi đúng.

-----

## 🛣️ Trạng thái phát triển (Roadmap)

  - [x] ✅ Cấu trúc POM cơ bản.
  - [x] ✅ Hoàn thiện các luồng Register, Login, Book Ticket.
  - [x] ✅ Xử lý My Ticket (Cancel, Filter).
  - [ ] 📄 Thêm Reporting (HTML Report).
  - [ ] 🤖 Tích hợp CI/CD (Jenkins/GitHub Actions).
  - [ ] 🌐 Hỗ trợ chạy đa trình duyệt (Firefox, Edge).

-----

*© 2025 VNUK Automation Project - Student Project*
