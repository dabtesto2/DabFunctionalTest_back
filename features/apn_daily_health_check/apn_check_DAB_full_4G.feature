  @apn_health_check_full
  Feature: Using Android Device check DAB FULL APN status using 4G

  Scenario Outline: With Android Device profile setup the context for <apn> with device profile <device_profile>
    Given Android device using "<device_profile>" select apn "<apn>" and wait for "<data_conn_wait>" sec
     When Network connection status is "Data" collect device information
     Then Data can be downloaded with "<device_profile>" and network "LTE,HSPAP,HSUPA,HSPA" wait for "<data_conn_wait>" sec
      And Open "chrome" browser and get url "<url>"
      And Check if page loads with "<title>" and click "<no_links>" links without error "ERR_TIMED_OUT"

    Examples:
      | apn                         | url                      | title  | no_links | data_conn_wait | device_profile |
      | idata-full-epg1             | https://www.google.co.uk | google | 2        | 5              | OA             |
      | mobile-full-epg1            | https://www.amazon.co.uk | amazon | 2        | 5              | NDS            |
      | ibrowse-full-epg1           | https://www.ebay.co.uk   | ebay   | 2        | 5              | OA             |
      | m-bb-full-epg1              | https://www.bbc.co.uk    | bbc    | 2        | 5              | PC             |
      | isetup-full-epg1            | https://www.amazon.co.uk | amazon | 2        | 5              | NDS            |
      | modem-full-epg1             | https://www.ebay.co.uk   | ebay   | 2        | 5              | OA             |
      | mvne1-full-epg1             | https://www.bbc.co.uk    | bbc    | 2        | 5              | PC             |
      | tesco-full-epg1             | https://www.amazon.co.uk | amazon | 2        | 5              | OA             |
      | payandgo-full-epg1          | https://www.google.co.uk | google | 2        | 5              | NDS            |
      | wap-full-epg1               | https://www.google.co.uk | google | 2        | 5              | OA             |
      | wap-full-epg1-legacy        | https://www.bbc.co.uk    | bbc    | 2        | 5              | PC             |
      | vpn-full-epg1               | https://www.ebay.co.uk   | ebay   | 2        | 5              | NDS            |
      | idata-full-epg2             | https://www.google.co.uk | google | 2        | 5              | OA             |
      | mobile-full-epg2            | https://www.amazon.co.uk | amazon | 2        | 5              | NDS            |
      | ibrowse-full-epg2           | https://www.ebay.co.uk   | ebay   | 2        | 5              | OA             |
      | m-bb-full-epg2              | https://www.bbc.co.uk    | bbc    | 2        | 5              | PC             |
      | isetup-full-epg2            | https://www.amazon.co.uk | amazon | 2        | 5              | NDS            |
      | modem-full-epg2             | https://www.ebay.co.uk   | ebay   | 2        | 5              | OA             |
      | mvne1-full-epg2             | https://www.bbc.co.uk    | bbc    | 2        | 5              | PC             |
      | tesco-full-epg2             | https://www.amazon.co.uk | amazon | 2        | 5              | NDS            |
      | payandgo-full-epg2          | https://www.google.co.uk | google | 2        | 5              | OA             |
      | wap-full-epg2               | https://www.google.co.uk | google | 2        | 5              | NDS            |
      | wap-full-epg2-legacy        | https://www.bbc.co.uk    | bbc    | 2        | 5              | PC             |
      | vpn-full-vepg-vpgw-2        | https://www.ebay.co.uk   | ebay   | 2        | 5              | NDS            |
      | idata-full-vepg-vpgw-2      | https://www.google.co.uk | google | 2        | 5              | OA             |
      | mobile-full-vepg-vpgw-2     | https://www.amazon.co.uk | amazon | 2        | 5              | NDS            |
      | ibrowse-full-vepg-vpgw-2    | https://www.ebay.co.uk   | ebay   | 2        | 5              | OA             |
      | m-bb-full-vepg-vpgw-2       | https://www.bbc.co.uk    | bbc    | 2        | 5              | PC             |
      | isetup-full-vepg-vpgw-2     | https://www.amazon.co.uk | amazon | 2        | 5              | OA             |
      | modem-full-vepg-vpgw-2      | https://www.ebay.co.uk   | ebay   | 2        | 5              | NDS            |
      | mvne1-full-vepg-vpgw-2      | https://www.bbc.co.uk    | bbc    | 2        | 5              | PC             |
      | tesco-full-vepg-vpgw-2      | https://www.amazon.co.uk | amazon | 2        | 5              | OA             |
      | payandgo-full-vepg-vpgw-2   | https://www.google.co.uk | google | 2        | 5              | NDS            |
      | wap-full-vepg-vpgw-2        | https://www.google.co.uk | google | 2        | 5              | OA             |
      | wap-full-vepg-vpgw-2-legacy | https://www.bbc.co.uk    | bbc    | 2        | 5              | PC             |
      | vpn-full-vepg-vpgw-2        | https://www.ebay.co.uk   | ebay   | 2        | 5              | NDS            |