# wechat-on-ai：微信高情商对话策略顾问

## 项目相关

### 项目介绍

本项目 `wechat-on-ai` 是一款基于微信和 `wxauto` 开发的智能对话策略顾问，旨在通过集成大语言模型（LLM）提升微信聊天体验。用户可通过小号登录并配置 AI 方向（基于 `system_prompt`），实现与 AI 微信好友的智能互动。鉴于同类项目可能面临的封号风险，本项目采用模拟人工操作的 RPA 方式，旨在降低风险。

本项目的核心目标是帮助用户提升聊天质量，尤其针对在社交互动中可能遇到的沟通障碍。通过多次优化 `prompt`，本项目致力于提供高效、流畅的对话支持，避免因沟通不畅导致的话题中断。相较于传统 AI 应用与微信之间的频繁切换和内容复制，`wechat-on-ai` 提供了一体化的解决方案，确保聊天记录的连续性和便捷性。

### 项目特点

1.  **RPA 模拟操作**：基于 `wxauto` 开发，通过模拟人工图形界面操作（RPA）方式与微信进行交互，有效降低因自动化操作导致的账号封禁风险（不活跃账号仍可能增加风险）。
2.  **智能文本对话**：支持与微信好友进行文本对话，并能智能解析和合并转发的聊天记录，确保对话内容的完整性与连贯性。

## 项目架构

本项目的文件结构清晰，各模块职责明确，便于理解和维护：

-   `.gitignore`: Git版本控制忽略文件配置，确保不提交不必要的文件。
-   `README.md`: 项目说明文档，包含项目介绍、安装、使用等指南。
-   `auto/client.py`: 微信客户端自动化操作模块，封装了微信消息监听和动作执行等功能。
-   `config.json.example`: 配置文件示例，用于配置微信和AI相关的参数。
-   `llm/llm.py`: 大语言模型交互模块，负责与OpenAI等大语言模型进行通信。
-   `llm/ml.py`: 机器学习相关代码，可能包含模型训练或数据处理逻辑。
-   `main.py`: 项目主入口，负责初始化、启动微信客户端和消息循环处理。
-   `requirements.txt`: Python依赖包清单，记录项目所需的所有库及其版本。
-   `utils/config.py`: 配置管理工具，用于加载和管理项目配置。
-   `utils/logger.py`: 日志记录工具，提供统一的日志输出功能。
-   `wechatbot.spec`: PyInstaller打包配置文件，用于将项目打包成可执行文件。


## 开发步骤

1.  **克隆项目到本地**：

    ```bash
    git clone https://github.com/PawNzZi/wechat-on-ai.git
    cd wechatbot
    ```

2.  **将 `config.json.exmaple` 文件改名为 `config.json`**：

    ```bash
    copy config.json.exmaple config.json
    ```
    或者手动复制并重命名。

3.  **创建虚拟环境并进入虚拟环境**：

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

4.  **`config.json` 填入相应的值**：
    打开 `config.json` 文件，根据注释或项目需求填入你的微信相关配置和 LLM API Key 等信息。

5.  **下载依赖文件**：

    ```bash
    pip install -r requirements.txt
    ```

6.  **运行 `python main.py` 文件**：

    ```bash
    python main.py
    ```

## 打包步骤

1.  **运行 `wechat-on-ai.spec` 文件生成 exe**：

    ```bash
    pyinstaller wechat-on-ai.spec
    ```

2.  **将自己的 `config.json` 文件放置同一目录下**：
    打包完成后，生成的 `wechat-on-ai.exe` 文件会在 `dist` 目录下。请将你的 `config.json` 文件复制到 `wechat-on-ai.exe` 所在的目录，以便程序能够正确读取配置。

## 使用指南

本项目专为 Windows 环境设计，因其依赖于微信客户端的桌面版操作。你可以在个人电脑或 Windows 服务器上部署运行。

### 1. 微信登录

在启动 `wechat-on-ai` 之前，请确保你的微信客户端已在运行环境中成功登录。

### 2. 配置 `config.json`

请仔细配置 `config.json` 文件。确保所有必要的参数（如 API 密钥、AI 行为设定等）均已正确填写。该文件应放置在 `main.py` 脚本或 `wechatbot.exe` 可执行文件的同级目录下，以便程序能够正确读取。

### 3. 启动程序

根据你的环境和需求，选择以下任一方式启动 `wechat-on-ai`：

*   **通过 Python 脚本运行 (需要 Python 环境)**：

    ```bash
    python main.py
    ```

*   **运行可执行文件 (无需 Python 环境)**：

    导航至 `dist` 目录下，双击 `wechat-on-ai.exe` 即可启动程序。
