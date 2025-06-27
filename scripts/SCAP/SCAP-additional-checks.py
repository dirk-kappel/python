import paramiko

# Define the remote server details
hostname = ""
port = 22
username = ""
key_path = ""  # Path to your SSH private key
root_password = ""  # Root password for the remote server

# Define the output file
output_file = "command_output.txt"

# Define the new commands structure
commands = [

    {"V-230222": ["sudo yum history list | more"]},
    {"V-230224": ["sudo blkid"]},
    {"V-230225": [
        "sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*banner'", 
        "cat /etc/issue"
    ]},
    {"V-230226": ["echo 'NA - graphical user interface not installed.'"]},
    {"V-230227": ["sudo cat /etc/issue"]},
    {"V-230228": ["sudo grep -E '(auth\.\*|authpriv\.\*|daemon\.\*)' /etc/rsyslog.conf /etc/rsyslog.d/*.conf"]},
    {"V-230229": ["sudo openssl x509 -text -in /etc/sssd/pki/sssd_auth_ca_db.pem | head -n 13"]},
    {"V-230230": ["echo 'NA - There are no private keys on the golden image.'"]},
    {"V-230240": ["sudo getenforce"]},
    {"V-230243": ["sudo find / -type d \( -perm -0002 -a ! -perm -1000 \) -print 2>/dev/null"]},
    {"V-230251": ["sudo grep -i macs /etc/crypto-policies/back-ends/opensshserver.config"]},
    {"V-230252": ["sudo grep -i ciphers /etc/crypto-policies/back-ends/opensshserver.config"]},
    {"V-230254": [
        "sudo grep -i opensslcnf.config /etc/pki/tls/openssl.cnf",
        "sudo update-crypto-policies --show"
    ]},
    {"V-230256": ["sudo grep -io +vers.* /etc/crypto-policies/back-ends/gnutls.config"]},
    {"V-230260": ["sudo find -L /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type f -exec ls -l {} \;"]},
    {"V-230261": ["sudo find -L /lib /lib64 /usr/lib /usr/lib64 ! -user root -exec ls -l {} \;"]},
    {"V-230262": ["sudo find -L /lib /lib64 /usr/lib /usr/lib64 ! -group root -exec ls -l {} \;"]},
    {"V-230263": [
        "sudo ls -al /etc/cron.* | grep aide",
        "sudo grep aide /etc/crontab /var/spool/cron/root",
        "sudo cat /etc/cron.daily/aide"
    ]},
    {"V-230274": ["sudo grep certificate_verification /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf | grep -v '^#'"]},
    {"V-230275": [
        "sudo yum list installed opensc",
        "sudo opensc-tool --list-drivers | grep -i piv"
    ]},
    {"V-230276": ["sudo dmesg | grep NX"]},
    {"V-230277": [
        "sudo grub2-editenv list | grep page_poison",
        "sudo grep page_poison /etc/default/grub"
    ]},
    {"V-230278": [
        "sudo grub2-editenv list | grep vsyscall",
        "sudo grep vsyscall /etc/default/grub"
    ]},
    {"V-230279": [
        "sudo grub2-editenv list | grep slub_debug",
        "sudo grep slub_debug /etc/default/grub"
    ]},
    {"V-230285": [
        "echo 'NA - RHEL version is 8.4 or newer.'",
        "cat /etc/redhat-release"
    ]},
    {"V-230299": [
        "sudo awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1,$3,$6}' /etc/passwd",
        "sudo cat /etc/fstab"
    ]},
    {"V-230302": [
        "sudo awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1,$3,$6}' /etc/passwd",
        "sudo cat /etc/fstab"
    ]},
    {"V-230303": ["sudo cat /etc/fstab"]},
    {"V-230304": ["sudo cat /etc/fstab"]},
    {"V-230305": ["sudo cat /etc/fstab"]},
    {"V-230309": [
        "sudo find /home -xdev -type f -perm -0002 -print",
        "sudo find /var -xdev -type f -perm -0002 -print",
        "sudo find /tmp -xdev -type f -perm -0002 -print",
        "sudo find /var/tmp -xdev -type f -perm -0002 -print",
        "sudo find /var/log -xdev -type f -perm -0002 -print",
        "sudo find /var/log/audit -xdev -type f -perm -0002 -print"
    ]},
    {"V-230310": ["sudo systemctl status kdump.service"]},
    {"V-230312": ["sudo systemctl status systemd-coredump.socket"]},
    {"V-230316": [
        "sudo grep hosts /etc/nsswitch.conf",
        "sudo ls -al /etc/resolv.conf",
        "sudo grep nameserver /etc/resolv.conf"
    ]},
    {"V-230317": ["sudo grep -i path= /home/*/.*"]},
    {"V-230318": [
        "sudo find /home -xdev -type d -perm -0002 -uid +999 -print",
        "sudo find /var -xdev -type d -perm -0002 -uid +999 -print",
        "sudo find /tmp -xdev -type d -perm -0002 -uid +999 -print",
        "sudo find /var/tmp -xdev -type d -perm -0002 -uid +999 -print",
        "sudo find /var/log -xdev -type d -perm -0002 -uid +999 -print",
        "sudo find /var/log/audit -xdev -type d -perm -0002 -uid +999 -print"
        ]},
    {"V-230319": [
        "sudo find /home -xdev -type d -perm -0002 -gid +999 -print",
        "sudo find /var -xdev -type d -perm -0002 -gid +999 -print",
        "sudo find /tmp -xdev -type d -perm -0002 -gid +999 -print",
        "sudo find /var/tmp -xdev -type d -perm -0002 -gid +999 -print",
        "sudo find /var/log -xdev -type d -perm -0002 -gid +999 -print",
        "sudo find /var/log/audit -xdev -type d -perm -0002 -gid +999 -print"
        ]},
    {"V-230320": [
        "sudo pwck -r",
        "sudo awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $3, $6}' /etc/passwd"
    ]},
    {"V-230321": ["sudo ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd)"]},
    {"V-230322": [
        "sudo ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd)",
        "sudo grep $(grep ec2-user /etc/passwd | awk -F: '{print $4}') /etc/group",
        "sudo grep $(grep ssm-user /etc/passwd | awk -F: '{print $4}') /etc/group"
    ]},
    {"V-230323": [
        "sudo ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd)",
        "sudo pwck -r"
    ]},
    {"V-230325": [
        "sudo ls -al /home/ec2-user/.[^.]* | more",
        "sudo ls -al /home/ssm-user/.[^.]* | more"
    ]},
    {"V-230326": ["sudo find / -fstype xfs -nouser"]},
    {"V-230327": ["sudo find / -fstype xfs -nogroup"]},
    {"V-230328": [
        "sudo awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1,$3,$6}' /etc/passwd",
        "sudo grep /home /etc/fstab"
    ]},
    {"V-230329": ["echo 'NA - graphical user interface not installed.'"]},
    {"V-230331": ["echo 'NA - No temporary accounts are created on the golden image.'"]},
    {"V-230338": [
        "echo 'NA - RHEL version is 8.2 or newer.'",
        "cat /etc/redhat-release"
    ]},
    {"V-230339": [
        "echo 'NA - RHEL version is 8.2 or newer.'",
        "cat /etc/redhat-release"
    ]},
    {"V-230347": ["echo 'NA - graphical user interface not installed.'"]},
    {"V-230349": [
        "sudo ps all | grep tmux | grep -v grep",
        "sudo grep -r tmux /etc/bashrc /etc/profile.d",
        "sudo cat /etc/profile.d/tmux.sh"
    ]},
    {"V-230351": ["echo 'NA - graphical user interface not installed.'"]},
    {"V-230352": ["echo 'NA - graphical user interface not installed.'"]},
    {"V-230353": ["sudo grep -i lock-after-time /etc/tmux.conf"]},
    {"V-230354": ["echo 'NA - graphical user interface not installed.'"]},
    {"V-230355": ["sudo cat /etc/sssd/sssd.conf"]},
    {"V-230371": ["sudo awk -F ':' 'list[$3]++{print $1, $3}' /etc/passwd"]},
    {"V-230372": ["echo 'NA - smart card logon not used.'"]},
    {"V-230374": ["echo 'NA - No temporary accounts are created on the golden image.'"]},
    {"V-230379": ["sudo cat /etc/passwd"]},
    {"V-230384": ["sudo grep -ir ^umask /home | grep -v '.bash_history'"]},
    {"V-230385": ["grep -i umask /etc/bashrc /etc/csh.cshrc /etc/profile"]},
    {"V-230387": [
        "sudo grep -s cron /etc/rsyslog.conf /etc/rsyslog.d/*.conf",
        "sudo grep -s /var/log/messages /etc/rsyslog.conf /etc/rsyslog.d/*.conf"
    ]},
    {"V-230389": ["sudo grep 'postmaster:\s*root$' /etc/aliases"]},
    {"V-230466": [
        "sudo grep dir /etc/security/faillock.conf",
        "sudo grep -w faillock /etc/audit/audit.rules"
    ]},
    {"V-230468": [
        "sudo grub2-editenv list | grep audit",
        "sudo grep audit /etc/default/grub"
    ]},
    {"V-230469": [
        "sudo grub2-editenv list | grep audit",
        "sudo grep audit /etc/default/grub"
    ]},
    {"V-230470": ["sudo grep -i auditbackend /etc/usbguard/usbguard-daemon.conf"]},
    {"V-230475": ["sudo grep -E '(\/usr\/sbin\/(audit|au|rsys))' /etc/aide.conf"]},
    {"V-230476": [
        "sudo grep -iw log_file /etc/audit/auditd.conf",
        "sudo df -h /var/log/audit/"
    ]},
    {"V-230479": ["sudo grep @@ /etc/rsyslog.conf /etc/rsyslog.d/*.conf"]},
    {"V-230481": [
        "sudo grep -i '$DefaultNetstreamDriver' /etc/rsyslog.conf /etc/rsyslog.d/*.conf",
        "sudo grep -i '$ActionSendStreamDriverMode' /etc/rsyslog.conf /etc/rsyslog.d/*.conf"
    ]},
    {"V-230482": ["sudo grep -i '$ActionSendStreamDriverAuthMode' /etc/rsyslog.conf /etc/rsyslog.d/*.conf"]},
    {"V-230484": [
        "sudo grep maxpoll /etc/chrony.conf",
        "sudo grep -i server /etc/chrony.conf"
    ]},
    {"V-230491": [
        "sudo grub2-editenv list | grep pti",
        "sudo grep pti /etc/default/grub"
    ]},
    {"V-230493": [
        "sudo grep -r uvcvideo /etc/modprobe.d/* | grep '/bin/false'",
        "sudo grep -r uvcvideo /etc/modprobe.d/* | grep 'blacklist'"
    ]},
    {"V-230500": ["sudo firewall-cmd --list-all-zones"]},
    {"V-230502": ["sudo systemctl status autofs"]},
    {"V-230504": ["echo 'NA - iptables used instead of firewalld.'"]},
    {"V-230505": ["sudo yum list installed firewalld"]},
    {"V-230506": ["sudo nmcli device status"]},
    {"V-230523": ["sudo yum list installed fapolicyd"]},
    {"V-230524": ["sudo usbguard list-rules"]},
    {"V-230525": ["echo 'NA - iptables used instead of firewalld.'"]},
    {"V-230529": ["sudo systemctl status ctrl-alt-del.target"]},
    {"V-230530": ["echo 'NA - graphical user interface not installed.'"]},
    {"V-230532": ["sudo systemctl status debug-shell.service"]},
    {"V-230551": ["sudo find / -name aide.conf"]},
    {"V-230552": [
        "sudo find / -name aide.conf",
        "sudo grep -E '[+]?acl' /etc/aide.conf"
    ]},
    {"V-230553": ["rpm -qa | grep xorg | grep server"]},
    {"V-230554": ["sudo ip link | grep -i promisc"]},
    {"V-244519": [
        "echo 'NA - graphical user interface not installed.'",
        "rpm -qa | grep xorg | grep server"
    ]},
    {"V-244521": ["sudo grep -iw 'superusers' /boot/efi/EFI/redhat/grub.cfg"]},
    {"V-244522": ["echo 'NA - system not booted with BIOS.'"]},
    {"V-244523": ["sudo grep sulogin-shell /usr/lib/systemd/system/emergency.service"]},
    {"V-244525": ["sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientaliveinterval'"]},
    {"V-244526": ["sudo grep CRYPTO_POLICY /etc/sysconfig/sshd"]},
    {"V-244527": ["sudo yum list installed rng-tools"]},
    {"V-244528": ["sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*gssapiauthentication'"]},
    {"V-244529": ["sudo grep /var/tmp /etc/fstab"]},
    {"V-244530": ["sudo mount | grep '\s/boot/efi\s'"]},
    {"V-244531": [
        "sudo ls -lLR /home/ec2-user",
        "sudo ls -lLR /home/ssm-user"
    ]},
    {"V-244532": [
        "sudo ls -ILR /home/ec2-user",
        "sudo ls -ILR /home/ssm-user",
        "sudo grep ec2-user /etc/group",
        "sudo grep ssm-user /etc/group"
    ]},
    {"V-244533": ["sudo grep pam_faillock.so /etc/pam.d/system-auth"]},
    {"V-244534": ["sudo grep pam_faillock.so /etc/pam.d/password-auth"]},
    {"V-244535 | V-244536 | V-244538 | V-244539": [
        "echo 'NA - graphical user interface not installed.'",
        "rpm -qa | grep xorg | grep server"
    ]},
    {"V-244537": ["sudo yum list installed tmux"]},
    {"V-244542": ["sudo systemctl status auditd.service"]},
    {"V-244543": ["sudo grep -w space_left_action /etc/audit/auditd.conf"]},
    {"V-244544": ["echo 'NA - iptables used instead of firewalld.'"]},
    {"V-244545": ["sudo systemctl status fapolicyd.service"]},
    {"V-244546": [
        "sudo grep permissive /etc/fapolicyd/fapolicyd.conf",
        "sudo tail /etc/fapolicyd/compiled.rules"
    ]},
    {"V-244547": ["sudo yum list installed usbguard"]},
    {"V-244548": ["sudo systemctl status usbguard.service"]},
    {"V-244549": ["sudo yum list installed openssh-server"]},
    {"V-244550": [
        "sudo sysctl net.ipv4.conf.default.accept_redirects",
        "sudo grep -r net.ipv4.conf.default.accept_redirects /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf"
    ]},
    {"V-244551": [
        "sudo sysctl net.ipv4.conf.all.accept_source_route",
        "sudo grep -r net.ipv4.conf.all.accept_source_route /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf"
    ]},
    {"V-244552": [
        "sudo sysctl net.ipv4.conf.default.accept_source_route",
        "sudo grep -r net.ipv4.conf.default.accept_source_route /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf"
    ]},
    {"V-244553": [
        "sudo sysctl net.ipv4.conf.all.accept_redirects",
        "sudo grep -r net.ipv4.conf.all.accept_redirects /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf"
    ]},
    {"V-245540": ["sudo /opt/McAfee/agent/scripts/ma status"]},
    {"V-250315": [
        "sudo grep -w dir /etc/security/faillock.conf",
        "sudo ls -Zd /var/log/faillock"
    ]},
    {"V-250316": [
        "echo 'NA - RHEL version is 8.2 or newer.'",
        "cat /etc/redhat-release"
    ]},
    {"V-250317": [
        "sudo sysctl net.ipv4.conf.all.forwarding",
        "sudo grep -r net.ipv4.conf.all.forwarding /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf"
    ]},
    {"V-251707": ["sudo find /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type d -exec stat -c '%n %a' '{}' \;"]},
    {"V-251708": ["sudo find /lib /lib64 /usr/lib /usr/lib64 ! -user root -type d -exec stat -c '%n %U' '{}' \;"]},
    {"V-251709": ["sudo find /lib /lib64 /usr/lib /usr/lib64 ! -group root -type d -exec stat -c '%n %G' '{}' \;"]},
    {"V-251710": [
        "sudo rpm -q aide",
        "sudo /usr/sbin/aide --check | head -n 20"
    ]},
    {"V-251711": [
        "sudo grep include /etc/sudoers",
        "sudo grep -r include /etc/sudoers.d"
    ]},
    {"V-251712": ["sudo grep pam_succeed_if /etc/pam.d/sudo"]},
    {"V-251713": ["sudo cat /etc/pam.d/system-auth | grep pam_pwquality"]},
    {"V-251715": [
        "echo 'NA - RHEL version is 8.4 or newer.'",
        "cat /etc/redhat-release"
    ]},
    {"V-251716": [
        "sudo grep -r retry /etc/security/pwquality.conf*",
        "sudo grep pwquality /etc/pam.d/system-auth /etc/pam.d/password-auth | grep retry"
    ]},
    {"V-251717": ["sudo grep -i remember /etc/pam.d/system-auth"]},
    {"V-251718": ["systemctl get-default"]},
    {"V-254520": ["sudo semanage login -l | more"]},
    {"V-255924": ["sudo grep -i kexalgorithms /etc/crypto-policies/back-ends/opensshserver.config"]},
    {"V-256973": [
        "sudo rpm -q --queryformat '%{SUMMARY}\n' gpg-pubkey | grep -i 'red hat'",
        "sudo gpg -q --keyid-format short --with-fingerprint /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release"
    ]},
    {"V-256974": ["sudo yum list installed mailx"]}
]

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote server using the SSH key
    client.connect(hostname, port=port, username=username, key_filename=key_path)

    with open(output_file, "w") as f:
        for control in commands:
            for control_name, commands in control.items():
                # Write the control name to the file
                f.write(f"Control: {control_name}\n")

                for cmd in commands:
                    # Write the command to the file
                    f.write(f"$ {cmd}\n")
                    print(f"Running command: {cmd}")
                    # Execute the command on the remote server
                    full_cmd = f"sudo su - -c '{cmd}'"
                    stdin, stdout, stderr = client.exec_command(full_cmd)

                    # Send the root password to stdin
                    stdin.write(root_password + "\n")
                    stdin.flush()

                    # Read the output and error streams
                    output = stdout.read().decode()
                    error = stderr.read().decode()

                    # Write the output to the file
                    if output:
                        f.write("\n")
                        f.write(output)
                    else:
                        f.write("No output received\n")

                    if error:
                        f.write("Error Output:\n")
                        f.write(error)

                    # Add a separator for readability between commands
                    f.write("----------------------------------------\n")

                # Add a separator for readability between controls
                f.write("========================================\n")

finally:
    # Close the SSH connection
    client.close()
