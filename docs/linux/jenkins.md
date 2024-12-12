# jenkins

## Jenkinsfile examples

Run ansible playbook
```yaml
pipeline {
    options {
        ansiColor('xterm')
    }

    agent {
        label 'agent-01'
    }

    parameters {
        string(name: 'DAYS', defaultValue: '90', description: 'Delete files that are older than this age [days]')
        booleanParam(name: 'REMOVE', defaultValue: "true", description: 'If set, files will be deleted')
        string(name: 'HOSTS', defaultValue: "test-ru-01", description: 'Hosts where to clear the logs [Example: test-en-0021,test-en-0019]')
    }

    stages {
        
        stage ('Prepare') {
            steps {
                sh "env"
            }
        }

        stage ('Get source code') {
            when {
                expression {params.HOSTS != ""}
            }
            steps {
                echo "\033[1;37;44mStage: ${env.STAGE_NAME}\033[0m"
                git branch: "master",
                    changelog: false,
                    credentialsId: 'some_id',
                    poll: false,
                    url: 'ssh://git@domain.com/DevOps/routing.git'
            }
        }
                
        stage('Execute script') {
            when {
                expression {params.HOSTS != ""}
            }
            steps {
                echo "\033[1;37;44mStage: ${env.STAGE_NAME}\033[0m"

                dir ('ansible') {
                    ansiblePlaybook (
                        colorized: true,
                        installation: 'ansible',
                        playbook: 'cleanup_disks.yml',
                        extraVars: [
                            days: "${params.DAYS}",
                            remove: "${params.REMOVE}",
                            variable_host: "${params.HOSTS}"
                        ],
                        extras: '-v'
                    )
                }
            }
        }
    }

    post {
        always {
            deleteDir()
        }
    }
}
```

Run playbook and shell script:
```yaml
pipeline {
    options {
        ansiColor('xterm')
    }

    agent {
        label 'bdcigate01'
    }

    parameters {
        string(name: 'HOSTS', defaultValue: "test-01", description: 'Hosts on which user home directories will be deleted [Example: test-02,test-03]')
        booleanParam(name: 'ARCHIVE', defaultValue: "false", description: 'If set, user folders will be archived')
    }

    stages {
        
        stage ('Prepare') {
            steps {
                sh "env"
            }
        }

        stage ('Get source code') {
            when {
                expression {params.HOSTS != ""}
            }
            steps {
                echo "\033[1;37;44mStage: ${env.STAGE_NAME}\033[0m"
                git branch: "master",
                    changelog: false,
                    credentialsId: 'cred_id',
                    poll: false,
                    url: 'ssh://git@domain.com/tasks.git'
            }
        }
                
        stage('Execute script') {
            when {
                expression {params.HOSTS != ""}
            }
            steps {
                echo "\033[1;37;44mStage: ${env.STAGE_NAME}\033[0m"
                dir ('ansible') {
                    ansiblePlaybook (
                        colorized: true,
                        installation: 'ansible',
                        playbook: 'cleanup_user_folders.yml',
                        extraVars: [
                            archive: "${params.ARCHIVE}",
                            variable_host: "${params.HOSTS}"
                        ],
                        extras: ''
                    )

                    script {
                        def list = "${params.HOSTS}".split(',')
                        def datetime = sh returnStdout: true, script: "date +%Y.%m.%d_%H.%M.%S"
                        for (int i = 0; i < list.size(); i++) {
                            sh """
                            set +x

                            echo "\033[1;30;43mScript result for ${list[i]}:\033[0m"

                            if (${params.ARCHIVE}); then
                              ssh -q -o IdentityFile=/data/jenkins/.ssh/ansible.key -o PasswordAuthentication=no -o User=ansible -o ConnectTimeout=10 ${list[i]} "sudo sh -c \'/data/cleanup_user_folders_has23dqw/env/bin/python3 /data/cleanup_user_folders_has23dqw/cleanup_user_folders.py -d /data/cleanup_user_folders/archive /data/cleanup_user_folders_has23dqw/user_list.txt\'"
                            else
                              ssh -q -o IdentityFile=/data/jenkins/.ssh/ansible.key -o PasswordAuthentication=no -o User=ansible -o ConnectTimeout=10 ${list[i]} "sudo sh -c \'/data/cleanup_user_folders_has23dqw/env/bin/python3 /data/cleanup_user_folders_has23dqw/cleanup_user_folders.py -t -d /data/cleanup_user_folders/archive /data/cleanup_user_folders_has23dqw/user_list.txt\'"
                            fi

                            """
                        }
                    }

                    ansiblePlaybook (
                        colorized: true,
                        installation: 'ansible',
                        playbook: 'cleanup_user_folders_end.yml',
                        extraVars: [
                            variable_host: "${params.HOSTS}"
                        ]
                    )
                }
            }
        }
    }

    post {
        always {
            deleteDir()
        }
    }
}
```