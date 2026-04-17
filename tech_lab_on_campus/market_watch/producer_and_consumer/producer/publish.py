#!/usr/bin/env python

# Copyright 2024 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python

import os
import sys
from solution.producer_sol import mqProducer  # pylint: disable=import-error


def main() -> None:
    if len(sys.argv) != 4:
        print("Usage: python publish.py <ticker> <price> <sector>")
        sys.exit(1)

    ticker = sys.argv[1]
    price = sys.argv[2]
    sector = sys.argv[3]

    exchange_name = "stocks_topic_exchange"
    routing_key = f"stock.{sector}.{ticker}"
    message = f"{ticker} is ${price}"

    producer = mqProducer(
        routing_key=routing_key,
        exchange_name=exchange_name,
    )
    producer.publishOrder(message)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)