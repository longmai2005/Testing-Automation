# 🚀 VNUK 2025: Selenium Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium)
![Pattern](https://img.shields.io/badge/Design%20Pattern-POM-orange?style=for-the-badge)

> Dự án kiểm thử tự động hóa cho ứng dụng web, được xây dựng dựa trên Selenium WebDriver và Python, áp dụng mô hình **Page Object Model (POM)** để tối ưu hóa khả năng bảo trì.


## 📂 Cấu trúc Dự án

Dự án được tổ chức theo mô-đun để dễ dàng mở rộng:

```text
selenium-python-example/
├── 📄 test_login.py         # Kịch bản kiểm thử (Test Scripts)
├── 📂 pages/                # Page Objects (POM)
│   ├── 🐍 login_page.py     # Các hành động trên trang Login
│   └── 🐍 home_page.py      # Các hành động trên trang Home
└── 📝 README.md             # Tài liệu dự án
````

-----

## 🛠️ Cài đặt & Yêu cầu

### Tiền điều kiện

  * **Python 3.x** đã được cài đặt.
  * **Google Chrome** trình duyệt mới nhất.
  * **ChromeDriver** tương thích với phiên bản Chrome của bạn.

### Hướng dẫn cài đặt nhanh

1.  **Clone repository về máy:**

    ```bash
    git clone [https://bitbucket.org/agestvn/vnuk-2025](https://bitbucket.org/agestvn/vnuk-2025)
    cd selenium-python-example
    ```

2.  **Cài đặt các thư viện cần thiết:**

    ```bash
    pip install selenium
    ```

-----

## ⚡ Hướng dẫn chạy Test

Bạn có thể chạy kiểm thử bằng một trong các lệnh sau:

| Mục tiêu | Lệnh thực thi |
| :--- | :--- |
| **Chạy cơ bản** | `python test_login.py` |
| **Dùng Unittest** | `python -m unittest test_login.py` |
| **Chế độ chi tiết (Verbose)** | `python -m unittest test_login.py -v` |

-----

## 🧩 Chi tiết Kiến trúc (Architecture)

### 1\. Test Cases (`test_login.py`)

| ID | Tên Test Case | Mô tả quy trình |
| :--- | :--- | :--- |
| **TC01** | `Login Functionality` | 1. Mở trang chủ <br> 2. Vào trang đăng nhập <br> 3. Nhập Email/Pass hợp lệ <br> 4. Xác nhận đăng nhập thành công |

### 2\. Page Objects

Chúng tôi tách biệt logic kiểm thử và giao diện người dùng:

  * **`pages/login_page.py`**: Quản lý các element như ô nhập liệu email, password và nút login. Cung cấp hàm `login(user, pass)`.
  * **`pages/home_page.py`**: Quản lý điều hướng và xác thực tin nhắn chào mừng (`get_welcome_msg`).

-----

## ⚙️ Cấu hình

  * **URL Kiểm thử:** `http://railwayb1.somee.com/`
  * **Trình duyệt mặc định:** Google Chrome (Thiết lập trong `setUp()`)

-----

## 🛣️ Roadmap & Cải tiến

Dưới đây là danh sách các tính năng dự kiến sẽ phát triển thêm:

  - [ ] 🔄 Thay thế `sleep()` bằng `WebDriverWait` (Explicit Wait).
  - [ ] 📄 Thêm file config (`config.ini` hoặc `.env`) để quản lý Test Data.
  - [ ] 📸 Tự động chụp màn hình (Screenshot) khi Test thất bại.
  - [ ] 📊 Xuất báo cáo kết quả kiểm thử dạng HTML.
  - [ ] 🌐 Hỗ trợ chạy đa trình duyệt (Firefox, Edge).

-----

## 🤝 Đóng góp

Dự án này phục vụ mục đích giáo dục. Mọi ý kiến đóng góp hoặc Pull Request đều được hoan nghênh\!

-----

*© 2025 VNUK Automation Project*

