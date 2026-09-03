class MerchantOmnichannelMarketingCampaignDesignerClient:
    def design_marketing_campaign(self, campaign_objective='Re-engage lapsed buyers who bought espresso machines in last 6 months', promotional_offer='20% off single-origin bean subscription', channels=['Email', 'SMS', 'Instagram Carousel']):
        return {
            'campaign_design_id': 'mkt_cmp_8812',
            'target_audience_segment_size': 4850,
            'projected_campaign_revenue_usd': 24200.00,
            'email_subject_line_variants': [
                'Elena, fresh roast alert: Take 20% off Ethiopia Yirgacheffe',
                'Elevate your morning espresso routine with fresh beans'
            ],
            'sms_copy_template': 'GenPark Coffee: Your machine misses you! Enjoy 20% off artisanal beans with code ROAST20: https://gpk.ai/r20',
            'human_approval_required_before_send': True,
            'campaign_asset_bundle_url': 'https://campaigns.merchant.genpark.ai/bundles/8812.json'
        }
