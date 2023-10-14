import os
from put_in_ap_mode import put_in_ap_mode

abs_dir = os.path.abspath("./")

with open("/etc/xdg/lxsession/LXDE-pi/autostart", "w") as file:
    file.write(f"@sudo {abs_dir}/start_api.bash {abs_dir}")

put_in_ap_mode()