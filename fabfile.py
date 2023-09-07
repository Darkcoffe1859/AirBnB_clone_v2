#!usr/bin/python3
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the web_static folder."""
    try:
        # Create the 'versions' directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Create the archive filename based on the current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"

        # Compress the contents of the web_static folder into the archive
        local("tar -czvf versions/{} web_static".format(archive_name))

        # Return the path to the created archive
        return "versions/{}".format(archive_name)

    except Exception:
        # Return None if an error occurs
        return None

