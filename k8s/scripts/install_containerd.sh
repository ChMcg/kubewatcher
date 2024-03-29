# Configure required modules

# First load two modules in the current running environment and configure them to load on boot

sudo modprobe overlay
sudo modprobe br_netfilter

cat <<EOF | sudo tee /etc/modules-load.d/containerd.conf
overlay
br_netfilter
EOF

# Configure required sysctl to persist across system reboots

cat <<EOF | sudo tee /etc/sysctl.d/99-kubernetes-cri.conf
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
net.bridge.bridge-nf-call-ip6tables = 1
EOF

# Apply sysctl parameters without reboot to current running enviroment

sudo sysctl --system

# Install containerd packages

sudo apt-get update 
sudo apt-get install -y containerd

# Create a containerd configuration file

sudo mkdir -p /etc/containerd
sudo containerd config default | sudo tee /etc/containerd/config.toml

# Set the cgroup driver for runc to systemd

# Set the cgroup driver for runc to systemd which is required for the kubelet.
# For more information on this config file see the containerd configuration docs here and also here.

# At the end of this section in /etc/containerd/config.toml
# 
#       [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
#       ...
# 
# Around line 112, change the value for SystemCgroup from false to true.
# 
#             SystemdCgroup = true
# 
# If you like, you can use sed to swap it out in the file with out having to manually edit the file.

sudo sed -i 's/            SystemdCgroup = false/            SystemdCgroup = true/' /etc/containerd/config.toml

# Restart containerd with the new configuration

sudo systemctl restart containerd

# And that's it, from here you can install and configure Kubernetes on top of this container runtime. In an upcoming post, I will bootstrap a cluster using containerd as the container runtime.

# источник: https://www.nocentino.com/posts/2021-12-27-installing-and-configuring-containerd-as-a-kubernetes-container-runtime/
