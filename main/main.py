from telegram.ext import Updater, CommandHandler


def code(update, context):
    a = ['update.message.animation()', 'update.message.audio()', 'update.message.author_signature()', 'update.message.bot()', 'update.message.caption()', 'update.message.caption_entities()', 'update.message.caption_html()', 'update.message.caption_html_urled()', 'update.message.caption_markdown()', 'update.message.caption_markdown_urled()', 'update.message.caption_markdown_v2()', 'update.message.caption_markdown_v2_urled()', 'update.message.channel_chat_created()', 'update.message.chat()', 'update.message.chat_id()', 'update.message.connected_website()', 'update.message.contact()', 'update.message.copy()', 'update.message.date()', 'update.message.de_json()', 'update.message.de_list()', 'update.message.delete()', 'update.message.delete_chat_photo()', 'update.message.dice()', 'update.message.document()', 'update.message.edit_caption()', 'update.message.edit_date()', 'update.message.edit_live_location()', 'update.message.edit_media()', 'update.message.edit_reply_markup()', 'update.message.edit_text()', 'update.message.effective_attachment()', 'update.message.entities()', 'update.message.forward()', 'update.message.forward_date()', 'update.message.forward_from()', 'update.message.forward_from_chat()', 'update.message.forward_from_message_id()', 'update.message.forward_sender_name()', 'update.message.forward_signature()', 'update.message.from_user()', 'update.message.game()', 'update.message.get_game_high_scores()', 'update.message.group_chat_created()', 'update.message.has_protected_content()', 'update.message.invoice()', 'update.message.is_automatic_forward()', 'update.message.left_chat_member()', 'update.message.link()', 'update.message.location()', 'update.message.media_group_id()', 'update.message.message_auto_delete_timer_changed()', 'update.message.message_id()', 'update.message.migrate_from_chat_id()', 'update.message.migrate_to_chat_id()', 'update.message.new_chat_members()', 'update.message.new_chat_photo()', 'update.message.new_chat_title()', 'update.message.parse_caption_entities()', 'update.message.parse_caption_entity()', 'update.message.parse_entities()', 'update.message.parse_entity()', 'update.message.passport_data()', 'update.message.photo()', 'update.message.pin()', 'update.message.pinned_message()', 'update.message.poll()', 'update.message.proximity_alert_triggered()', 'update.message.reply_animation()', 'update.message.reply_audio()', 'update.message.reply_chat_action()', 'update.message.reply_contact()', 'update.message.reply_copy()', 'update.message.reply_dice()', 'update.message.reply_document()', 'update.message.reply_game()', 'update.message.reply_html()', 'update.message.reply_invoice()', 'update.message.reply_location()', 'update.message.reply_markdown()', 'update.message.reply_markdown_v2()', 'update.message.reply_markup()', 'update.message.reply_media_group()', 'update.message.reply_photo()', 'update.message.reply_poll()', 'update.message.reply_sticker()', 'update.message.reply_text()', 'update.message.reply_to_message()', 'update.message.reply_venue()', 'update.message.reply_video()', 'update.message.reply_video_note()', 'update.message.reply_voice()', 'update.message.sender_chat()', 'update.message.set_game_score()', 'update.message.sticker()', 'update.message.stop_live_location()', 'update.message.stop_poll()', 'update.message.successful_payment()', 'update.message.supergroup_chat_created()', 'update.message.text()', 'update.message.text_html()', 'update.message.text_html_urled()', 'update.message.text_markdown()', 'update.message.text_markdown_urled()', 'update.message.text_markdown_v2()', 'update.message.text_markdown_v2_urled()', 'update.message.to_dict()', 'update.message.to_json()', 'update.message.unpin()', 'update.message.venue()', 'update.message.via_bot()', 'update.message.video()', 'update.message.video_chat_ended()', 'update.message.video_chat_participants_invited()', 'update.message.video_chat_scheduled()', 'update.message.video_chat_started()', 'update.message.video_note()', 'update.message.voice()', 'update.message.voice_chat_ended()', 'update.message.voice_chat_participants_invited()', 'update.message.voice_chat_scheduled()', 'update.message.voice_chat_started()', 'update.message.web_app_data()',
         'update.effective_chat.all_members_are_administrators()', 'update.effective_chat.approve_join_request()', 'update.effective_chat.ban_chat()', 'update.effective_chat.ban_member()', 'update.effective_chat.ban_sender_chat()', 'update.effective_chat.bio()', 'update.effective_chat.bot()', 'update.effective_chat.can_set_sticker_set()', 'update.effective_chat.copy_message()', 'update.effective_chat.create_invite_link()', 'update.effective_chat.de_json()', 'update.effective_chat.de_list()', 'update.effective_chat.decline_join_request()', 'update.effective_chat.description()', 'update.effective_chat.edit_invite_link()', 'update.effective_chat.export_invite_link()', 'update.effective_chat.first_name()', 'update.effective_chat.full_name()', 'update.effective_chat.get_administrators()', 'update.effective_chat.get_member()', 'update.effective_chat.get_member_count()', 'update.effective_chat.get_members_count()', 'update.effective_chat.get_menu_button()', 'update.effective_chat.has_private_forwards()', 'update.effective_chat.has_protected_content()', 'update.effective_chat.has_restricted_voice_and_video_messages()', 'update.effective_chat.id()', 'update.effective_chat.invite_link()', 'update.effective_chat.join_by_request()', 'update.effective_chat.join_to_send_messages()', 'update.effective_chat.kick_member()', 'update.effective_chat.last_name()', 'update.effective_chat.leave()', 'update.effective_chat.link()', 'update.effective_chat.linked_chat_id()', 'update.effective_chat.location()', 'update.effective_chat.message_auto_delete_time()', 'update.effective_chat.permissions()', 'update.effective_chat.photo()', 'update.effective_chat.pin_message()', 'update.effective_chat.pinned_message()', 'update.effective_chat.promote_member()', 'update.effective_chat.restrict_member()', 'update.effective_chat.revoke_invite_link()', 'update.effective_chat.send_action()', 'update.effective_chat.send_animation()', 'update.effective_chat.send_audio()', 'update.effective_chat.send_chat_action()', 'update.effective_chat.send_contact()', 'update.effective_chat.send_copy()', 'update.effective_chat.send_dice()', 'update.effective_chat.send_document()', 'update.effective_chat.send_game()', 'update.effective_chat.send_invoice()', 'update.effective_chat.send_location()', 'update.effective_chat.send_media_group()', 'update.effective_chat.send_message()', 'update.effective_chat.send_photo()', 'update.effective_chat.send_poll()', 'update.effective_chat.send_sticker()', 'update.effective_chat.send_venue()', 'update.effective_chat.send_video()', 'update.effective_chat.send_video_note()', 'update.effective_chat.send_voice()', 'update.effective_chat.set_administrator_custom_title()', 'update.effective_chat.set_menu_button()', 'update.effective_chat.set_permissions()', 'update.effective_chat.slow_mode_delay()', 'update.effective_chat.sticker_set_name()', 'update.effective_chat.title()', 'update.effective_chat.to_dict()', 'update.effective_chat.to_json()', 'update.effective_chat.type()', 'update.effective_chat.unban_chat()', 'update.effective_chat.unban_member()', 'update.effective_chat.unban_sender_chat()', 'update.effective_chat.unpin_all_messages()', 'update.effective_chat.unpin_message()', 'update.effective_chat.username()',
         'update.effective_user.added_to_attachment_menu()', 'update.effective_user.approve_join_request()', 'update.effective_user.bot()', 'update.effective_user.can_join_groups()', 'update.effective_user.can_read_all_group_messages()', 'update.effective_user.copy_message()', 'update.effective_user.de_json()', 'update.effective_user.de_list()', 'update.effective_user.decline_join_request()', 'update.effective_user.first_name()', 'update.effective_user.full_name()', 'update.effective_user.get_menu_button()', 'update.effective_user.get_profile_photos()', 'update.effective_user.id()', 'update.effective_user.is_bot()', 'update.effective_user.is_premium()', 'update.effective_user.language_code()', 'update.effective_user.last_name()', 'update.effective_user.link()', 'update.effective_user.mention_button()', 'update.effective_user.mention_html()', 'update.effective_user.mention_markdown()', 'update.effective_user.mention_markdown_v2()', 'update.effective_user.name()', 'update.effective_user.pin_message()', 'update.effective_user.send_action()', 'update.effective_user.send_animation()', 'update.effective_user.send_audio()', 'update.effective_user.send_chat_action()', 'update.effective_user.send_contact()', 'update.effective_user.send_copy()', 'update.effective_user.send_dice()', 'update.effective_user.send_document()', 'update.effective_user.send_game()', 'update.effective_user.send_invoice()', 'update.effective_user.send_location()', 'update.effective_user.send_media_group()', 'update.effective_user.send_message()', 'update.effective_user.send_photo()', 'update.effective_user.send_poll()', 'update.effective_user.send_sticker()', 'update.effective_user.send_venue()', 'update.effective_user.send_video()', 'update.effective_user.send_video_note()', 'update.effective_user.send_voice()', 'update.effective_user.set_menu_button()', 'update.effective_user.supports_inline_queries()', 'update.effective_user.to_dict()', 'update.effective_user.to_json()', 'update.effective_user.unpin_all_messages()', 'update.effective_user.unpin_message()', 'update.effective_user.username()',
         'context.bot.addStickerToSet()', 'context.bot.add_sticker_to_set()', 'context.bot.answerCallbackQuery()',
         'context.bot.answerInlineQuery()', 'context.bot.answerPreCheckoutQuery()', 'context.bot.answerShippingQuery()',
         'context.bot.answerWebAppQuery()', 'context.bot.answer_callback_query()', 'context.bot.answer_inline_query()',
         'context.bot.answer_pre_checkout_query()', 'context.bot.answer_shipping_query()',
         'context.bot.answer_web_app_query()', 'context.bot.approveChatJoinRequest()',
         'context.bot.approve_chat_join_request()', 'context.bot.arbitrary_callback_data()',
         'context.bot.banChatMember()', 'context.bot.banChatSenderChat()', 'context.bot.ban_chat_member()',
         'context.bot.ban_chat_sender_chat()', 'context.bot.base_file_url()', 'context.bot.base_url()',
         'context.bot.bot()', 'context.bot.callback_data_cache()', 'context.bot.can_join_groups()',
         'context.bot.can_read_all_group_messages()', 'context.bot.close()', 'context.bot.commands()',
         'context.bot.copyMessage()', 'context.bot.copy_message()', 'context.bot.createChatInviteLink()',
         'context.bot.createInvoiceLink()', 'context.bot.createNewStickerSet()',
         'context.bot.create_chat_invite_link()', 'context.bot.create_invoice_link()',
         'context.bot.create_new_sticker_set()', 'context.bot.de_json()', 'context.bot.de_list()',
         'context.bot.declineChatJoinRequest()', 'context.bot.decline_chat_join_request()', 'context.bot.defaults()',
         'context.bot.deleteChatPhoto()', 'context.bot.deleteChatStickerSet()', 'context.bot.deleteMessage()',
         'context.bot.deleteMyCommands()', 'context.bot.deleteStickerFromSet()', 'context.bot.deleteWebhook()',
         'context.bot.delete_chat_photo()', 'context.bot.delete_chat_sticker_set()', 'context.bot.delete_message()',
         'context.bot.delete_my_commands()', 'context.bot.delete_sticker_from_set()', 'context.bot.delete_webhook()',
         'context.bot.editChatInviteLink()', 'context.bot.editMessageCaption()',
         'context.bot.editMessageLiveLocation()', 'context.bot.editMessageMedia()',
         'context.bot.editMessageReplyMarkup()', 'context.bot.editMessageText()', 'context.bot.edit_chat_invite_link()',
         'context.bot.edit_message_caption()', 'context.bot.edit_message_live_location()',
         'context.bot.edit_message_media()', 'context.bot.edit_message_reply_markup()',
         'context.bot.edit_message_text()', 'context.bot.exportChatInviteLink()',
         'context.bot.export_chat_invite_link()', 'context.bot.first_name()', 'context.bot.forwardMessage()',
         'context.bot.forward_message()', 'context.bot.getChat()', 'context.bot.getChatAdministrators()',
         'context.bot.getChatMember()', 'context.bot.getChatMemberCount()', 'context.bot.getChatMembersCount()',
         'context.bot.getChatMenuButton()', 'context.bot.getCustomEmojiStickers()', 'context.bot.getFile()',
         'context.bot.getGameHighScores()', 'context.bot.getMe()', 'context.bot.getMyCommands()',
         'context.bot.getMyDefaultAdministratorRights()', 'context.bot.getStickerSet()', 'context.bot.getUpdates()',
         'context.bot.getUserProfilePhotos()', 'context.bot.getWebhookInfo()', 'context.bot.get_chat()',
         'context.bot.get_chat_administrators()', 'context.bot.get_chat_member()',
         'context.bot.get_chat_member_count()', 'context.bot.get_chat_members_count()',
         'context.bot.get_chat_menu_button()', 'context.bot.get_custom_emoji_stickers()', 'context.bot.get_file()',
         'context.bot.get_game_high_scores()', 'context.bot.get_me()', 'context.bot.get_my_commands()',
         'context.bot.get_my_default_administrator_rights()', 'context.bot.get_sticker_set()',
         'context.bot.get_updates()', 'context.bot.get_user_profile_photos()', 'context.bot.get_webhook_info()',
         'context.bot.id()', 'context.bot.insert_callback_data()', 'context.bot.kickChatMember()',
         'context.bot.kick_chat_member()', 'context.bot.last_name()', 'context.bot.leaveChat()',
         'context.bot.leave_chat()', 'context.bot.link()', 'context.bot.logOut()', 'context.bot.log_out()',
         'context.bot.logger()', 'context.bot.name()', 'context.bot.pinChatMessage()', 'context.bot.pin_chat_message()',
         'context.bot.private_key()', 'context.bot.promoteChatMember()', 'context.bot.promote_chat_member()',
         'context.bot.request()', 'context.bot.restrictChatMember()', 'context.bot.restrict_chat_member()',
         'context.bot.revokeChatInviteLink()', 'context.bot.revoke_chat_invite_link()', 'context.bot.sendAnimation()',
         'context.bot.sendAudio()', 'context.bot.sendChatAction()', 'context.bot.sendContact()',
         'context.bot.sendDice()', 'context.bot.sendDocument()', 'context.bot.sendGame()', 'context.bot.sendInvoice()',
         'context.bot.sendLocation()', 'context.bot.sendMediaGroup()', 'context.bot.sendMessage()',
         'context.bot.sendPhoto()', 'context.bot.sendPoll()', 'context.bot.sendSticker()', 'context.bot.sendVenue()',
         'context.bot.sendVideo()', 'context.bot.sendVideoNote()', 'context.bot.sendVoice()',
         'context.bot.send_animation()', 'context.bot.send_audio()', 'context.bot.send_chat_action()',
         'context.bot.send_contact()', 'context.bot.send_dice()', 'context.bot.send_document()',
         'context.bot.send_game()', 'context.bot.send_invoice()', 'context.bot.send_location()',
         'context.bot.send_media_group()', 'context.bot.send_message()', 'context.bot.send_photo()',
         'context.bot.send_poll()', 'context.bot.send_sticker()', 'context.bot.send_venue()',
         'context.bot.send_video()', 'context.bot.send_video_note()', 'context.bot.send_voice()',
         'context.bot.setChatAdministratorCustomTitle()', 'context.bot.setChatDescription()',
         'context.bot.setChatMenuButton()', 'context.bot.setChatPermissions()', 'context.bot.setChatPhoto()',
         'context.bot.setChatStickerSet()', 'context.bot.setChatTitle()', 'context.bot.setGameScore()',
         'context.bot.setMyCommands()', 'context.bot.setMyDefaultAdministratorRights()',
         'context.bot.setPassportDataErrors()', 'context.bot.setStickerPositionInSet()',
         'context.bot.setStickerSetThumb()', 'context.bot.setWebhook()',
         'context.bot.set_chat_administrator_custom_title()', 'context.bot.set_chat_description()',
         'context.bot.set_chat_menu_button()', 'context.bot.set_chat_permissions()', 'context.bot.set_chat_photo()',
         'context.bot.set_chat_sticker_set()', 'context.bot.set_chat_title()', 'context.bot.set_game_score()',
         'context.bot.set_my_commands()', 'context.bot.set_my_default_administrator_rights()',
         'context.bot.set_passport_data_errors()', 'context.bot.set_sticker_position_in_set()',
         'context.bot.set_sticker_set_thumb()', 'context.bot.set_webhook()', 'context.bot.stopMessageLiveLocation()',
         'context.bot.stopPoll()', 'context.bot.stop_message_live_location()', 'context.bot.stop_poll()',
         'context.bot.supports_inline_queries()', 'context.bot.to_dict()', 'context.bot.to_json()',
         'context.bot.token()', 'context.bot.unbanChatMember()', 'context.bot.unbanChatSenderChat()',
         'context.bot.unban_chat_member()', 'context.bot.unban_chat_sender_chat()',
         'context.bot.unpinAllChatMessages()', 'context.bot.unpinChatMessage()',
         'context.bot.unpin_all_chat_messages()', 'context.bot.unpin_chat_message()', 'context.bot.uploadStickerFile()',
         'context.bot.upload_sticker_file()', 'context.bot.username()']


    print([f"update.message.{i}()" for i in dir(update.message) if i[0] != "_" and i[0] != i[0].upper()])
    print([f"update.effective_chat.{i}()" for i in dir(update.effective_chat) if i[0] != "_" and i[0] != i[0].upper()])
    print([f"update.effective_user.{i}()" for i in dir(update.effective_user) if i[0] != "_" and i[0] != i[0].upper()])
    print([f"context.bot.{i}()" for i in dir(context.bot) if i[0] != "_" and i[0] != i[0].upper()])


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', code))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
