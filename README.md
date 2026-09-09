# SPRING-CLOUD-S05-EX03: Cấu hình Chiến lược Cân bằng tải Random LoadBalancer

## Giới thiệu
Bài tập này hướng dẫn cách thay đổi thuật toán cân bằng tải mặc định từ **Round Robin** sang **Random LoadBalancer** cho dịch vụ `product-service` trong hệ thống Spring Cloud API Gateway.

## Chức năng đã thực hiện
1. **Khai báo cấu hình Java**:
    - Lớp `RandomLoadBalancerConfig` tạo Bean `ReactorLoadBalancer<ServiceInstance>` trả về một thực thể `RandomLoadBalancer`.
    - Lớp `GatewayApplication` khai báo annotation `@LoadBalancerClient(name = "product-service", configuration = RandomLoadBalancerConfig.class)` để áp dụng cấu hình ngẫu nhiên dành riêng cho `product-service`.
2. **Mô phỏng chương trình (Python)**:
    - Cung cấp file `main.py` giả lập lại quy trình phân phối request qua thuật toán Round Robin và Random Load Balancer để so sánh kết quả trực quan.

## Hướng dẫn chạy chương trình mô phỏng Python

Để chạy file mô phỏng và kiểm chứng thuật toán phân phối request ngẫu nhiên:

```bash
python main.py
```