from pathlib import Path
from typing import Final, Union

# 1階層上のディレクトリ
PROJECT_ROOT: Final[Path] = Path(__file__).parents[1]


def ensure_dir(path: Union[Path, str]) -> Path:
    """
    指定されたパスが存在するかチェックし、なければ作成する。
    絶対パス/相対パスで指定可能
    :param path:
    :return:
    """
    if not isinstance(path, (Path, str)):
        raise TypeError("path is must be pathlib.Path or str")
    path = Path(path)
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    return path


def get_project_root(as_str: bool = False) -> Union[Path, str]:
    """
    プロジェクトルートを取得する。
    :param as_str:
    :return:
    """
    if as_str:
        return str(PROJECT_ROOT)
    else:
        return PROJECT_ROOT
