import json
import os
import sys

def load_config():
    # config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')
    # 判断是否运行在PyInstaller打包的环境中
    if getattr(sys, 'frozen', False):
        # 如果是打包后的exe，使用sys._MEIPASS获取资源路径
        base_path = os.path.dirname(sys.executable)
    else:
        # 否则，使用常规的__file__路径
        base_path = os.path.dirname(os.path.dirname(__file__))

    config_path = os.path.join(base_path, 'config.json')
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # Validate required fields
    required_fields = {
        "monitor_user": "监控用户",
        "llm.base_url": "LLM基础URL",
        "llm.api_key": "LLM API密钥",
        "llm.model": "LLM模型",
        "llm.max_token": "LLM最大token",
        "llm.system_prompt": "LLM系统提示"
    }

    for key, description in required_fields.items():
        parts = key.split('.')
        current_value = config
        for part in parts:
            if isinstance(current_value, dict) and part in current_value:
                current_value = current_value[part]
            else:
                raise ValueError(f"配置项 '{description}' ({key}) 未找到或为空，请检查 config.json 文件。")
        
        # Special handling for monitor_user which can be an empty list but not None/empty string
        if key == "monitor_user":
            if not isinstance(current_value, list):
                raise ValueError(f"配置项 '{description}' ({key}) 格式不正确，应为列表。")
            # Allow empty list for monitor_user
        elif not current_value:
            raise ValueError(f"配置项 '{description}' ({key}) 未填写，请检查 config.json 文件。")

    return config