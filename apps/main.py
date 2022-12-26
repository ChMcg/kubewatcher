from kubernetes import client, config
import kubernetes as k8s


config.load_kube_config()



def main():
    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    a = [(i.status.pod_ip, i.metadata.namespace, i.metadata.name) for i in ret.items]
    print("\n".join(str(x) for x in a))
    
    v1.get_api_resources()
    




if __name__=="__main__":
    main()
