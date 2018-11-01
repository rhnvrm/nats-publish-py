from nats_publish import NatsPublish

np = NatsPublish(conn_options={
            "hostname": "demo.nats.io",
            "port": 4222,
        })

np.publish(msg='hello world', subject="foo")