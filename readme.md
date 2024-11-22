CRM System Documentation
1. Giới thiệu

Hệ thống CRM System là một giải pháp quản lý khách hàng và sản phẩm. Hệ thống này cung cấp:

    API để quản lý khách hàng, sản phẩm, giao dịch, cơ hội bán hàng, và yêu cầu hỗ trợ.
    Giao diện quản trị cho phép quản lý dữ liệu một cách dễ dàng thông qua trình duyệt.

2. Yêu cầu hệ thống

    Python: >= 3.9
    Django: >= 4.0
    PostgreSQL: >= 12.0
    pip: >= 20.0

3. Cài đặt và triển khai ứng dụng
3.1. Clone repository

Sao chép mã nguồn từ repository:
3.2 Cài đặt các dependencies
pipenv install

3.3. Cấu hình cơ sở dữ liệu
1. Mở file crm_project/settings.py
2. Thay đổi thông tin cấu hình PostgreSQL như sau:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crm_database',
        'USER': 'crm_user',
        'PASSWORD': 'your_secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

3.4. Chạy migrations

Khởi tạo và áp dụng migrations cho cơ sở dữ liệu:

python manage.py makemigrations
python manage.py migrate

3.5. Chạy server
Chạy server cục bộ:
python manage.py runserver

3.6. Tạo tài khoản quản trị viên
Tạo tài khoản admin để truy cập giao diện quản trị:
python manage.py createsuperuser

Nhập các thông tin cần thiết như username, email và password.
4. API Documentation

Dưới đây là danh sách các API chính được cung cấp bởi hệ thống.

4.1. API Quản lý Khách hàng
GET /api/customers/ Lấy danh sách khách hàng  body:None
POST /api/customers/ Thêm khách hàng mới body: { "name": "John", "email": "...", "phone": "..." }
GET /api/customers/<id>/ Lấy chi tiết khách hàng body: None
PUT /api/customers/<id>/ Cập nhật thông tin khách hàng body: { "name": "John Updated" }
DELETE /api/customers/<id>/ Xóa khách hàng body: None

4.2. API Quản lý Sản phẩm
4.3. API Quản lý Giao dịch
GET /api/transactions/ Lấy danh sách giao dịch None
POST /api/transactions/ body: { "customer": 1, "product": 2, "quantity": 3 }
4.4. API Quản lý Yêu cầu Hỗ trợ
GET /api/support-tickets/ Lấy danh sách yêu cầu hỗ trợ body: None

5. Sử dụng giao diện quản trị
    Tao tai khoan admin:
    python manage.py createsuperuser
    Truy cập URL: http://127.0.0.1:8000/admin/.
    Đăng nhập bằng tài khoản admin
    Quản lý dữ liệu:
        Customers: Thêm, sửa, hoặc xóa khách hàng.
        Products: Quản lý sản phẩm.
        Transactions: Theo dõi giao dịch.
        Leads: Quản lý cơ hội bán hàng.
        Support Tickets: Theo dõi và xử lý yêu cầu hỗ trợ.

6. Ví dụ mẫu dữ liệu
6.1. Mẫu dữ liệu cho Khách hàng

[
    {
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "phone": "123456789",
        "address": "123 Elm Street"
    },
    {
        "name": "Bob Brown",
        "email": "bob.brown@example.com",
        "phone": "987654321",
        "address": "456 Oak Avenue"
    }
]

6.2. Mẫu dữ liệu cho Sản phẩm
[
    {
        "name": "Laptop",
        "description": "High-performance laptop.",
        "price": 1500.50,
        "stock_quantity": 10
    },
    {
        "name": "Smartphone",
        "description": "Latest model smartphone.",
        "price": 999.99,
        "stock_quantity": 50
    }
]
