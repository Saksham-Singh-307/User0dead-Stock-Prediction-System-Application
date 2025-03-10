# paypal_config.py
import paypalrestsdk

paypalrestsdk.configure({
    "mode": "sandbox",  # or "live" for production
    "client_id": "AcwnBExRnkcEB5m6sVFco0ZikZA5VuZnGK89zG2uLJ2Pw1EywS-So8A9SB7739vzOGareryL2O54w1MA",
    "client_secret": "EN7lDf81Qh04-ZajW5YQccBfUO5hj3IklvXJ24BXC_q4Qpdy9kjWmm5v_dqWgHIF6GztVblxLvL6iWeY"
})