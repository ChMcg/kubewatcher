kubeadm join 45.85.117.217:6443 --token f9pdga.66y7u641xphkgq2c \
	--discovery-token-ca-cert-hash sha256:e04522c9a0e7e52d772e0da871e7854e1c915461ee2a970869f4551885b65428

kubeadm join \
	45.85.117.217:6443 2>&1 \
	--token 0fgb5d.u9somt6e4zd3e9ge \
	--discovery-token-ca-cert-hash \
	sha256:e04522c9a0e7e52d772e0da871e7854e1c915461ee2a970869f4551885b65428 \
	| tee kubeadm_join.log \
	| ccze -A
