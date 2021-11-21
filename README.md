# api_test

接口测试

## 接口安全测试

- OWSAP 服务端安全测试体系
    - 移动端安全
    - 服务端安全
- 模拟测试环境
    - DVWA 安全漏洞合集，[地址](https://dvwa.co.uk/)
        - 把 dvwa 拷贝到 xmapp/htdocs
        - 复制 config.inc.php.dist 为 config.inc.php
    - window 部署 DVWA 需要安装 xampp，[地址](https://www.apachefriends.org/index.html)
        - xampp-control 用于启动控制面板
            - config，如果之前安装过 apache、mysql、tomcat，就需要点击 config，在 Service and Port Settings 中设置端口
            - 如果需要修改端口，需要修改各个配置文件
            - 默认安装路径是根目录 '/xampp'，可以快速替换为 'C:/xampp'
        - 打开 http://localhost:8081/dvwa/setup.php，查看所有配置都生效，然后点下面的确认就行
        - 打开 http://localhost:8081/dvwa/login.php，默认登录密码和账号为 admin、password

### 常见安全漏洞

- Brute Force 暴力破解
- Command Injection 命令注入
- CSRF 跨站请求伪造
- File Inclusion 文件包含
- File Upload 文件上传
- Insecure CAPTCHA 不安全验证码
- SQL Injection SQL注入
- SQL Injection (Blind) SQL盲注
- Weak Session IDs 弱会话ID
- XSS (DOM) 基于DOM树的一种代码注入攻击方式
- XSS (Reflected) 反射型XSS是非持久性、参数型的跨站脚本
- XSS (Stored) 存储型跨站脚本攻击会把用户输入的数据存储在服务器端
- CSP Bypass 
- JavaScript 

```php
// 反射型 XSS（Low 等级）
<?php
header ("X-XSS-Protection: 0");
// Is there any input?
if( array_key_exists( "name", $_GET ) && $_GET[ 'name' ] != NULL ) {
    // Feedback for end user
    echo '<pre>Hello ' . $_GET[ 'name' ] . '</pre>';
}
?>
// 注入代码
?name=<script>alert("XSS");</script>.
```

常见安全工具
- OWASP ZAP
- WVS
- AppScan
- BurpSuite
- Sqlmap

建立安全测试流程
- 白盒代码分析：sonar、findbugs等
- 黑盒扫描机制：zap、wvs、burpsuite、appscan、sqlmap
- 业务流程安全探索：burpsuite、zap


测试



















