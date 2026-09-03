from client import MerchantOmnichannelMarketingCampaignDesignerClient

def main():
    client = MerchantOmnichannelMarketingCampaignDesignerClient()
    res = client.design_marketing_campaign('Summer clearance sale', '15% off outdoor gear')
    print('Merchant Marketing Campaign Designer: ' + res['campaign_design_id'])
    print('Audience Size: ' + str(res['target_audience_segment_size']) + ' | Projected Revenue: $' + str(res['projected_campaign_revenue_usd']))
    print('Top Email Subject: "' + res['email_subject_line_variants'][0] + '"')
    print('Bundle URL: ' + res['campaign_asset_bundle_url'])

if __name__ == '__main__':
    main()
