# Kind Cluster for ArgoCD Demo

## How to Install

1. create kind cluster:
```kind create cluster --config config.yaml```

2. install argocd
```kubectl create ns argocd```  
```kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml```

3. Patch Service to be NodePort type
```kubectl patch svc argocd-server -n argocd -p '{"spec": { "type": "NodePort", "ports": [{ "port": 80, "targetPort": 8080, "nodePort": 30080 }] }}'```

4. Get password
```kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo```

5. Deploy via github
Manually via UI


## Ports

localhost:30080 - argocd
localhost:30081 - webserver
localhost:30082 - webserver2