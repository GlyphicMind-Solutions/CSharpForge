# csharpforge.py
# Launcher for CSharpForge
# Created By: David Kistner (Unconditional Love) at GlyphicMind Solutions LLC.



#system imports
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication

#local imports
from engine.llm_engine import LLMEngine
from gui.csharpforge_window import CSharpForgeWindow



# ------------
# Main
# ------------
def main():
    base_dir = Path(__file__).parent.resolve()

    manifest_path = base_dir / "models" / "manifest.yaml"
    storage_root = base_dir / "storage"

    (storage_root / "logs").mkdir(parents=True, exist_ok=True)
    (storage_root / "pending").mkdir(parents=True, exist_ok=True)
    (storage_root / "saved").mkdir(parents=True, exist_ok=True)

    llm = LLMEngine(manifest_path)

    app = QApplication(sys.argv)
    window = CSharpForgeWindow(llm, storage_root)
    window.show()

    sys.exit(app.exec_())

# --------------------------
# if name = main windower
# --------------------------
if __name__ == "__main__":
    main()

