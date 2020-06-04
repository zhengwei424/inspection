production_envs = [
    {
        'name': '联通财务公司外网微服务区',
        'host': 'https://10.123.14.55:6443',
        'token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLTk2ZDduIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJhZWRmZWQzMi1hOTRlLTExZTktYWQ1ZC02YzkyYmZkNTQ4ODIiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.NPaCiGKMqwlkhjqPFjhw6D5_wIV03oo3vgDiZf18Nnf0TezxerTA6wvFWIm00uJa5Do_z2b0hlzb20zkX9N2erDJI8aPcb-J2Gp4ucC1ehnHBV_7KRsrV2GgKaBUYbQLTbj9_iNgPbMQrCGLyHBu1GYY86pW9ZucZaHrWC7f0f66v15PZSaxbxbG-Akt0Q806KB-Em3WyejgM0QQfmoMf_Qco9nkBuU6q4XEAeklUwSQu2SYNjXPh415CV8MWwomFjwFjrCFeZpizLO71Vx4_PpanzdhbRvpMmVYaJ0CaySmzsiGvQkDQp8OLBmtuo4Ra-pkpw2dIhgF67mBw03bMQ',
        'projects': {
            '6c142e16264740489eb87750d6aa14a4-fcp-outer-microservice': {
                '监管报送': {
                    '350b27f6414e40769650504f9faa59ef-fcp-outer-microservice': 'crisservice',
                    '40ce227f05bd47a197730d20d02fa84d-fcp-outer-microservice': 'crisview'
                }
            },
            '7505e75cfbc74e3b81b2592273a540f3-fcp-outer-microservice': {
                '公共服务': {
                    '8775dbf63b0048eea8dd0154f42e671b-fcp-outer-microservice': 'pubservice'
                }
            },
            '82a1880da1b544a582cc6e133febc3b8-fcp-outer-microservice': {
                '司库': {
                    '25da49734fca4251a50611fcd6ea0e11-fcp-outer-microservice': 'treasurerjob',
                    '9951d8af63e342f2bba45cad5bf28e71-fcp-outer-microservice': 'treasurerview',
                    '4bf9aa296fb246bab58c4acb5ea062e2-fcp-outer-microservice': 'treasurerservice'
                }
            },
            '10b5d426dea1448b8ac3fad727eda2dc-fcp-outer-microservice': {
                'bpm-审批域中台': {
                    'cd1e58e1b840463c90282aff0b22e035-fcp-outer-microservice': 'bpmservice'
                }
            },
            '9efff7f47f7b4f7583127851146cac7d-fcp-outer-microservice': {
                '公共管理': {
                    '9819c48eb3c441a1aaa6d89ced26d032-fcp-outer-microservice': 'pubview'
                }
            },
            'c95216c44f6e406997390bd908fff962-fcp-outer-microservice': {
                '内容影像': {
                    '9dfd6b6a64374f33b690e3bfb2bec86f-fcp-outer-microservice': 'vimservice',
                    '2bd6073b2bea4489b625d12d49a4de06-fcp-outer-microservice': 'ecmssearchservice',
                    'b09c1033e03e4c438d3e4dfe1360dfe0-fcp-outer-microservice': 'ecmsftsservice',
                    'c1520756067e4fa1936ebb14c2d26c80-fcp-outer-microservice': 'ecmscommonservice'
                }
            },
            '6cd297e121f148fab73f0090417edbe3-fcp-outer-microservice': {
                'asm事后监督系统': {
                    'bb1f54e042e143b0bc43aeeb6ced0e78-fcp-outer-microservice': 'asmservice',
                    '23d9b46b1bdc488fb34773531b6a142f-fcp-outer-microservice': 'asmview'
                }
            },
            '66df708708474b34a459bf04c8a73cc2-fcp-outer-microservice': {
                '平台公共服务': {
                    '2048888304b34a9db3548ca8da381ff7-fcp-outer-microservice': 'deposit',
                    'c20bd093d4704164bb914995a37c682d-fcp-outer-microservice': 'pubdata',
                    'b79867ca8db340d091d029c60abcfd33-fcp-outer-microservice': 'fcpcode'
                }
            }
        }
    },

    {
        'name': '联通财务公司外网后台区',
        'host': 'https://10.123.14.24:6443',
        'token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLXFxZGhyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIxYjIzZDFiMy1hOTRlLTExZTktYWYxNi02YzkyYmZkM2MwYjAiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.jwxyNTXSwuURfBUffqB8NFBD44TMG2iVg77Cy3i7WVU0SvBAjuDPxYbhttzbX-2xp4DzxlsX4__THSnOEAX4SQBykf8Iad0SjxJktxFHok66VJ0pz0Db1wpC2-lOrYa8lkwXOQAH7SdUAzhHnqzDutFrcHtYR-wHM8XEgvhmf8OXl_W2D9oSy2BvdJC6ysaKn3QpA0zIamlZWxeuaszSo7PL9FXOhqFaIpMghD9DhvHcN4-hLDbO8tpQKDab84lupu0lh25EGG0BwQ4kRv4IZnish84vjTzDpqNB-5cSHbmmqk5bBpL0KTatE6G38btaWWeGD8NDOaKliIi7E1fWZg',
        'projects': {
            'a542d960d3bc4f4aa1a5b193291c2998-fcp-outer-backend': {
                '决策分析': {
                    '06abcf4a357b4fdc8207af1e21515ace-fcp-outer-backend': 'decisionserver',
                    '02ea0264ba2b463787bfa93b4ef12873-fcp-outer-backend': 'decisionbi'
                }
            },
            'c82194ba3af84e06a0b7a6413fb31cf2-fcp-outer-backend': {
                'bps-流程引擎后台': {
                    'c3dd6308023e4ef8bc76e172c4612f72-fcp-outer-backend': 'bpsworkspace',
                    'fcab8e4ce5b14894a6c8c5e7b41e5741-fcp-outer-backend': 'bpsserver'
                }
            },
            '149f389b3fec4d17a80d077f84c486dd-fcp-outer-backend': {
                'ESB': {
                    '65cb0216d52c4d3f9e26bb94b78a34d8-fcp-outer-backend': 'esb-server2',
                    'b76ffdee694f400a88d0717d48b24b1a-fcp-outer-backend': 'esb-server1',
                    'e79eaefad06b40c486714906018e5420-fcp-outer-backend': 'esb-dangban'
                }
            },
            'dcb8a27ee8064ee78f3fcbdbbabcce0f-fcp-outer-backend': {
                '投资管理系统': {
                    '53f33ad1712e493d8379a7bf8834bc2e-fcp-outer-backend': 'xquant-xir2',
                    '5ea0c6eb5e564470bdd045cd7bbe1b21-fcp-outer-backend': 'xquant-calc2',
                    '8af7f46ff3984b4388bb6401856a78b3-fcp-outer-backend': 'xquant-calc',
                    '1c0eef3f2605484daaa331ac249ef8db-fcp-outer-backend': 'xquant-xir'
                }
            }
        }
    },

    {
        'name': '联通财务公司内网微服务区',
        'host': 'https://10.123.12.39:6443',
        'token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLXZwYjI1Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI5NGIzNzljNi1hOTRkLTExZTktOTkwYi02YzkyYmZkNjAwNWUiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.E-4ZYqvzYdudpW3USsxf6Cswx1PVm8HDZ71LxEAA4bExEUEMlbatkG-o-N6M0vyLeljyR_O_y05PEYKOVRHCfL96Y_KgUNErFglFt-hXJC5bYwBfiva8986iZwteq2bCG7o8Hk9-bqxWNFZqZRMnEm4fbnL--1x1Tju2r1zPSaRQx5q5XDAKYHoaw0erHbS08eUQUjAVEWco2VG08CYdnBDATF3u8fvxiKj8x78rfFzu4Qmb4kSZWFto78Urb5HFO-j4DzPfmvj9QR0fbybrnXQK_OHZNt4Zu5iMvWeUaEoUzo4M08Yy55zi23o-XccIcQMn3ZMLTPtyDfhdO2g8cg',
        'projects': {
            'f7e35b2438ec4029b713f0aa5e4a19c7-fcp-inner-microservice': {
                '消息中心': {
                    '26423a0098a04e30959a42e20151895c-fcp-inner-microservice': 'msgcenterservice',
                    '4daa938d07804c3686b6dd660bde688d-fcp-inner-microservice': 'msgcenterserviceconsumer'
                }
            },
            '04fadaa5cb654b97a45d6c2b79242391-fcp-inner-microservice': {
                '统一接入平台': {
                    'd5eb10cb0d1c4649a3b7729fb07f2be0-fcp-inner-microservice': 'uapservice'
                }
            },
            'ae3ce9d37f3241d79406ba7f3fe979f7-fcp-inner-microservice': {
                '客户信息管理系统': {
                    '9b642022371b40d0ab3f276bf62512c8-fcp-inner-microservice': 'ecifservice'
                }
            },
            '81f4126e11b74bf3a5c7cd64dfb032d0-fcp-inner-microservice': {
                '核心': {
                    '30ec57fdbf7444c5a15bceccf71de009-fcp-inner-microservice': 'ebankservice',
                    '8fdade24cd764cdba93c0d9784301a2f-fcp-inner-microservice': 'ebankview',
                    'a480ab6e7c044682bc81df4e30c1b50a-fcp-inner-microservice': 'cmsview',
                    'f936fa35d6fe4d158d7dbc0df772c791-fcp-inner-microservice': 'bedcservice',
                    '2bd40bcb686a4c84b34d1a0966bfa0ea-fcp-inner-microservice': 'evsservice',
                    '7b16b34bcd6941cab517e92354ca59ed-fcp-inner-microservice': 'cmsservice'
                }
            }
        }
    },
    {
        'name': '联通财务公司内网后台区',
        'host': 'https://10.123.12.55:6443',
        'token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLXZxamZtIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJkNzA2MGIyZS1hOTNkLTExZTktYjg3OC02YzkyYmZkM2I3NjgiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.qaEdB_3y6aDl0q6c9r6BhqtvPArxRTkkcjIuyvjEqvCzEuNDSDCQMlRjpuqMJ8n8PNza7wUcX00xNP3yYM7oLzTaerCHxAPK8bvqEID3LlUY-huTzpLLuSEo0hC2u0RkZm9dbivKrwT7pyauiBkaGZXBqmITVv_L7aOfaQSaqMQqQa3iYWnYjxSKxAZxjx8D1v0IuqsvmYabqRkMzkjo-Sot2GJm8E-0m5aTjKsKbEqQFOgYL7Cz5rn8_-tubV3v1KrJeU5f79wF1dShTtpiY31Ax3j56P3j8QJv-75_a86QjnPlBCBvHfc5CvjWv8Y98hSegR8jknoKonK55KuGjQ',
        'projects': {
            '3c2558da75bf4e0580ec305b8b80c510-fcp-inner-backend': {
                '数据仓库': {
                    'a29063d118a5461289998e6e021084e5-fcp-inner-backend': 'odsctlsagent2',
                    '07912ec616c24010951657fc49a1d6e8-fcp-inner-backend': 'odsctlsagent1',
                    'd8f40605007c48efae8c32effd7c077d-fcp-inner-backend': 'odsctlmagent',
                    '29d8877b716a480fa31f9c6a6390b6fb-fcp-inner-backend': 'odsctlmain'
                }
            },
            '81f4126e11b74bf3a5c7cd64dfb032d0-fcp-inner-backend': {
                '核心': {
                    '214e37d69557432c9fe36371c687bcbb-fcp-inner-backend': 'rdpcw',
                    'c994b24863924c769ff4c551abd6cd8f-fcp-inner-backend': 'v7cw'
                }
            }
        }
    },
    {
        'name': '联通财务公司慧企平台集群',
        'host': 'https://10.123.12.74:6443',
        'token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLW50d2RzIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJkZTQ3ZTg5MS1hOTM4LTExZTktYmNjOC02YzkyYmZkNzM4MTgiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.bZ-J6dkhaWBkAhavo5Ier9qTjA-J9WzoiiN8czcSS2icM9FsGZ7Mu8WJxP7tGqoEe0WSgb_4WogQUS_AnTy8_Xjxyo-q80oCHh3CYx5SLL_0_bPg-ak5fsfBGYsibhfc9AfpvFWrg4-M1rCLNPjQbdxvguddYNpyzukTGFDemwsvk3-3WFrZaTjzM9OuAYyBj2TOhVeV4QQ0PoHTwfNIWdQFL5ZiaN7p5YzdL9CEsgFfTwM3hNAlSuvMkB1AbBtOA3Atwd24mfCpytjtlgoXqvsaPTimu-XgWGOo_zIvjze-fSxYe0ihzv1PB_SIzr3n_LE9ozdneifI7iesr4wSTA',
        'projects': {
            # namespace
            '82f277bd-58d4-dd52-f78b-e8dcb1eccec7': {
                # 项目名称
                'dashboard-proxy': {
                    # deployment对应应用名称
                    'cdd6ab6c-ac03-2b6e-188c-3d74f8bdbc79': 'dashboard-proxy'
                }

            },
            'b81d947d-f50e-6ad6-a5eb-2e7d5f8f48fc': {
                '负载前后端': {
                    '96f28aaa-9511-13b2-7078-d029ce96e049': '负载均衡',
                    'efa582f1-3f4e-a7af-e309-867bdb09297f': '负载前端'
                }

            },
            '94ce6f4aeed743f182285f980ee10a51-k8s-mcloud': {
                '金融服务平台微服务组件': {
                    'msmp-zipkin-server': '服务跟踪'
                }

            },
            'ccfbd1c0-5cbe-963b-c1f0-0440ed217c5c': {
                '日志前后端': {
                    '50965108-c54a-ff90-6a53-b92eca61a0e1': '日志前端服务',
                    '0415eefc-87b3-8535-3f3a-c457b19c6421': '容器化后台实时日志'
                }

            },
            'msmp-backend': {
                'msmp-backend': {
                    'msmp-sms': 'msmp-sms',
                    'msmp-cicd': 'msmp-cicd',
                    'msmp-zipkin-server': '服务跟踪',
                    'msmp-turbine-server': 'msmp-turbine-server',
                    'msmp-openapi': 'msmp-openapi',
                    'msmp-view': '微服务管理平台VIEW前端',
                    'msmp-oauth2': 'msmp-oauth2',
                    'msmp-ui': '微服务管理平台前端',
                    'msmp-gateway-server': 'msmp-gateway-server',
                    'msmp-api': 'msmp-api',
                    'msmp-web': 'msmp-web',
                    'msmp-config-server': 'msmp-config-server',
                    'msmp-devopssso': 'msmp-devopssso',
                    'msmp-core': 'msmp-core'
                }

            },
            'containerization': {
                '容器化管理平台后台': {
                    'cmp-ui': '容器化管理平台UI',
                    'cmp': '容器化管理平台'
                }

            }
        }
    },
]
