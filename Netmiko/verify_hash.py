hash_match(local_file):
  with open (local_file) as file_to_check:
    data = file_to_check.read()
    md5_original = hashlib.md5(data).hexdigest()

  output = switch.ssh_connection.send_command('verify /md5' + remote_file)
  md5_flash = re.search(r'=\s+(\S+)', output)

  if md5_flash and (md5_original == md5_flash_group(1)):
    return true
  else:
    if md5_flash:
      print(f"MD5 verification failed")
      return false