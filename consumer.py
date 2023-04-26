from azure.eventhub import EventHubConsumerClient


def get_messages():
    connection_str = '<YOUR EVENTHUB CONNECTION STR>'
    consumer_group = '<YOUR CONSUMER GROUP NAME>'
    eventhub_name = '<YOUR EVENTHUB NAME>'
    client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group, eventhub_name=eventhub_name)


    def on_event_batch(partition_context, events):
        print("Received event from partition {}".format(partition_context.partition_id))
        print(len(events))
        # Checking whether there is any event returned as we have set max_wait_time
        if (len(events) == 0):
            # closing the client if there is no event triggered.
            client.close()

        else:
            for event in events:
                # Event.body operation
                print(
                    'Received the event: "{}" from the partition with ID: "{}"'.format(
                        event.body_as_str(encoding="UTF-8"), partition_context.partition_id
                    ))

    with client:
        client.receive_batch(
            on_event_batch=on_event_batch,
            starting_position="-1", max_wait_time=5, max_batch_size=2  # "-1" is from the beginning of the partition.
        )


get_messages()
