## HttpRunner

HttpRunner 
- 是一款面向 HTTP(S) 协议的通用测试框架
- 只需编写维护一份 YAML/JSON 脚本，即可实现自动化测试、性能测试、线上监控、持续集成等多种测试需求
- Python 环境：支持 3.6/3.7/3.8
    - venv 虚拟环境：python3 -m venv ~/.venv/httprunner、source ~/.venv/httprunner/bin/active
    - 测试：httprunner -V，hrun -V
    - 使用脚手架：httprunner startproject -h，httprunner startproject demo
        - 运行脚手架：hrun demo